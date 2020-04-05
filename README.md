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
    - remove polish accents 
    - all leters to lowercase
    - remove control characters
    - remove digits 
    - concatenate divided words
    - replace non-alphanum with space  
    - replace multiple spaces with single space 
    - remove short words
    - remove stop-words
    - stemming 
2. Processing: 
    - count occurrences of words 
    - calculate TFIDF
    - select n top keywords
3. Doc2Vec
4. Visualization 
    - PCA
5. Cluster analysis
    - KMeans

## References:  
 [1]: http://www.gutenberg.org/
