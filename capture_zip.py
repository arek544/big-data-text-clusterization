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

import os, errno
import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

sc = SparkContext(conf=SparkConf())
spark = SparkSession(sparkContext=sc)

books_rdd = spark.sparkContext.textFile("data/*")