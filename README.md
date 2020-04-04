# Big data text clusterization
Project team: Arkadiusz Sycz, Michał Wojeciechowski, Stanisław Puchała

## Goals

Visualization and clusterization big amount of text documents. We'll use dump of Freebase [1] - base of a general-knowledge facts. Original Freebase [2] is designed as an open, community-curatedknowledge base with more than 40 million topics and over 2 billion facts.

Processing will be done with the use of a multithreaded mapp reduce algorithm.

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
    - count occurences of words 
    - calculate TFIDF
    - salect n top key words
3. Doc2Vec
4. Visualization 
5. Cluster analysis

Bibliography:  
    [1]: Data source: http://freebase-easy.cs.uni-freiburg.de/dump/  
    [2]: K. D. Bollacker, C. Evans, P. Paritosh, T. Sturge, andJ. Taylor. Freebase: a collaboratively created graphdatabase for structuring human knowledge. InSIGMOD, pages 1247–1250, 2008.  

---
Interesting articles:  
    https://www.kdnuggets.com/2017/06/text-clustering-unstructured-data.html  
    https://github.com/vivekkalyanarangan30/Text-Clustering-API/  
