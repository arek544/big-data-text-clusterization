# Big data text clusterization
Project team: Arkadiusz Sycz, Michał Wojeciechowski, Stanisław Puchała

## Goals

Visualization and clusterization big amount of text documents. 

### Steps:

1. Scrapp english books in txt format from Project Gutenberg web site [1].
2. Preprocess, vectorize and present each book in spatial representation. 
3. Describe resulting clusters by the concurrent keyword (or set of keywords) in a given cluster. 

Processing will be done with the use of a multithreade mapp reduce algorithm. 

## To do:
1. Preprocessing:
    - remove accents 
    - all leters to lowercase
    - remove control characters
    - remove digits 
    - concatenate divided words
    - replace non-alphanum with space  
    - replace multiple spaces with single space 
    - remove stop-words
    - stemming: (SnowballStemmer, WordNetLemmatizer)
2. Processing: 
    - count occurrences of words 
    - calculate TFIDF
3. Visualization 
    - visualization of explained variance
    - PCA
4. Cluster analysis
    - selecting the number of clusters 
    - KMeans

References:  
    [1]: http://www.gutenberg.org/
