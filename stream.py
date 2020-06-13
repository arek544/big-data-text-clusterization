# -*- coding: utf-8 -*-

# Sergei Bugrov
# 7-9-17
#
# Downloads all available books in English language in .txt format from http://www.gutenberg.org,
# unpacks them from .zip archives, saves them to ../books/ folder, and deletes .zip files.
#
# usage : python gutenberg.py
#
# python version : 3.6.1
# https://cognitivedemons.wordpress.com/2017/07/10/downloading-all-english-books-from-gutenberg-org-with-python/

import os
import re
import unidecode
from pyspark.sql.types import StringType, ArrayType
from pyspark import SparkContext, SparkConf, Row
from pyspark.sql.functions import udf
from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer, StopWordsRemover,HashingTF, IDF
from pyspark.ml import Pipeline
from nltk.stem.snowball import SnowballStemmer

def list_stemmer(words):
    stemmer = SnowballStemmer(language='english')
    return [stemmer.stem(word) for word in words]

def clean(text):
    text = unidecode.unidecode(text) # remove accents
    text = text.lower()
    text = text.replace(r'\n','') # remove newline sign
    text = re.sub(r'\d+', '', text) # remove digits 
    text = re.sub(r'[.]?-[.]?', '', text) # concatenate divided words
    text = re.sub(r'[\W]+',' ', text) # replace non-alphanum with space  
    text = re.sub(' +', ' ', text) # replace multiple spaces with single space 
    return text

def process_rdd(text_id,text):
    row = Row(id=text_id, text=text)
    rdd = sc.parallelize([row])
    df = rdd.flatMap(lambda x: (x,)).toDF() 
    df.show()
    user_def_fun = udf(f=clean, returnType=StringType())

    df = df.withColumn("cleaned", user_def_fun("text"))
    df = df.drop('text')

    tokenizer = Tokenizer(inputCol="cleaned", outputCol="tokens")
    df = tokenizer.transform(df)
    df.show()
    df = df.drop('cleaned')
    

    stopword_removal = StopWordsRemover(inputCol='tokens', 
                                    outputCol='refined_tokens')
    df = stopword_removal.transform(df)
    # df.show(2)
    df = df.drop('tokens')

    stemming = udf(list_stemmer, returnType=ArrayType(StringType()))

    df = df.withColumn("stem", stemming("refined_tokens"))

    df = df.drop("refined_tokens")

    hashing_vec = HashingTF(numFeatures=1000,
                            inputCol='stem',
                            outputCol='tf_features')

    hashing_df = hashing_vec.transform(df)

    hashing_df.cache()
    tf_idf_vec = IDF(inputCol='tf_features',
                outputCol='tf_idf_features')

    tf_idf_df = tf_idf_vec.fit(hashing_df).transform(hashing_df)
    # tf_idf_df.select(['stem','tf_idf_features']).show(2)
    tf_idf_df = tf_idf_df.drop(*['stem','tf_features']) 
    tf_idf_df.show()

sc = SparkContext(conf=SparkConf())
spark = SparkSession(sparkContext=sc)

fileDirectory = 'data_small/'

for fname in os.listdir(fileDirectory):
    text = open(fileDirectory+fname).read()
    process_rdd(fname.replace('.txt',''),text)