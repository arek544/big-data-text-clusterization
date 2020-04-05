# Big data text clusterization
Project team: Arkadiusz Sycz, Michał Wojeciechowski, Stanisław Puchała

## Goals

Visualization and clusterization big amount of text documents. We'll scrapp english books in txt format from Project Gutenberg web site, preprocess, vectorize and present them in spatial representation. Processing will be done with the use of a multithreade mapp reduce algorithm.

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
    - stemming 
2. Processing: 
    - count occurrences of words 
    - calculate TFIDF
    - select n top keywords
3. Doc2Vec
4. Visualization 
5. Cluster analysis

References:  
    [1]: Data scraper: https://gist.github.com/mbforbes/cee3fd5bb3a797b059524fe8c8ccdc2b
    [2]: http://www.gutenberg.org/

---
Interesting articles:  
    https://webapps.stackexchange.com/questions/12311/how-to-download-all-english-books-from-gutenberg
    https://www.kdnuggets.com/2017/06/text-clustering-unstructured-data.html  
    https://github.com/vivekkalyanarangan30/Text-Clustering-API/  
