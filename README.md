# Programming-project

## Specifications

This project is composed of two python files and twelve html files:

•	**Operations.py**, where there are two classes, one named gff3_databasereader, thanks to which we were able to read the GFF3 file and transforming it into a readable dataset for the user. This was also thanks to the use of pandas, which is an open source Python package that is most widely used for data science/data analysis and machine learning tasks. The other class was named gff3_database, which contains eleven functions that have various aims, such as:
1.	obtaining basic information about the dataset and return a  list of unique sequence IDs, name, source and type
2.	obtaining the list of unique type of operations available in the dataset
3.	counting the number of features provided by the same source
4.	counting the number of entries for each type of operation
5.	deriving a new dataset containing only the information about entire chromosomes.
6.	calculating the fraction of unassembled sequences from source GRCh38
7.	obtaining a new dataset containing only entries from source ensembl, havana and ensembl_havana
8.	counting the number of entries for each type of operation for the dataset containingonly entries from source ensembl , havana and ensembl_havana
9.	returning the gene names from the dataset containing containing only entries from source ensembl , havana and ensembl_havana

•	**App.py**, where ,with the help of Flask, pandas and Operations.py, we were able to implement the Web-based user interface 

•	**Html files**, each file corresponded to an active function in the gff3_database class, plus an homepage where you can se the description of our project and choose which operations you want to see

## Templates
This folder contains the templates that were used to implement **App.py** to create the Web page

## Data

Here you can download the dataset that we worked on, which is a GFF file , commonly used to analyse genomic data 

https://www.dropbox.com/s/11yzbl0dpyanvyi/Homo_sapiens.GRCh38.85.gff3.gz?dl=0

If you want to know more about this kind of files, here we provide a link with exaustive explenations about GFF3

https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md

## Libraries
During this project we used pandas and Flask, importing them in the files:

```import pandas as pd
from flask import Flask, render_template
```

## CRC Cards
We provide the Class Responsibility Collaboration Cards inside our website, where we describe the design of our Software. Said cards were created with the help of **Visual Paradigm**

## Creators 
Arianna Bellezza, Francesco Luciano Cocci
