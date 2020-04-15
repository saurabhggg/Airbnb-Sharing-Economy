# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 00:27:16 2020

@author: Saurabh Gupta
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

import gensim
from gensim import corpora, models
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
np.random.seed(2018)
nltk.download('wordnet')
from array import array


def lemmatize_stemming(text):
    return SnowballStemmer("english").stem(WordNetLemmatizer().lemmatize(text, pos='v'))
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result


dataset = pd.read_csv('california_hotelroom.csv')

host_review = dataset.iloc[:,[13]].values
textt = []
for i in range(len(host_review)):
    splitted = host_review[i][0].split(", '")
    for k in range(len(splitted)):
        textt.append(splitted[k])
        
host_review = textt
    


processed_docs = []
for i in range(len(host_review)):
    arr = preprocess(host_review[i])
    print('arr = ' + str(arr))
    processed_docs.append(arr)
    
dictionary = gensim.corpora.Dictionary(processed_docs)
print(dictionary)
count = 0
for k, v in dictionary.iteritems():
    print('k = ' + str(k))
    print('v = ' + str(v))
    count += 1
    if count > 10:
        break

dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100)
bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]


tfidf = models.TfidfModel(bow_corpus)
corpus_tfidf = tfidf[bow_corpus]

from pprint import pprint
for doc in corpus_tfidf:
    pprint(doc)
    break


lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=10, id2word=dictionary, passes=2, workers=2)

for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))
    
    
lda_model_tfidf = gensim.models.LdaMulticore(corpus_tfidf, num_topics=10, id2word=dictionary, passes=2, workers=4)
for idx, topic in lda_model_tfidf.print_topics(-1):
    print('Topic: {} Word: {}'.format(idx, topic))
    


import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects.packages import importr
import rpy2.robjects as R

import rpy2
rpy2.__path__
sentiment_by = importr('sentimentr')

x = textt[0]

activity = R.r(r'''
               function(x){
               print(x)
               a = sentiment_by(x)
               return(a)
               }'''
               
               )

review = dataset.iloc[:,[13]].values
arr = [0]*100

for i in range(len(review)):
    splitted = review[i][0].split(", '")
    sums = 0
    for k in range(len(splitted)):
        summ = activity(splitted[k])
        a = (R.r['as.numeric'](summ))
        sums = sums + a[3]
        
    print('sum = ' + str(sums))
    print('length = ' + str(len(splitted)))
    sums = sums/len(splitted)
    arr[i] = sums
    
    
arr2 = [0]*100 
review = dataset.iloc[:,[13]].values
for i in range(len(review)):
    splitted = review[i][0].split(", '")
    print('split = ' + str(splitted))
    summm = 0
    countt = 0
    for k in range(len(splitted)):
        words = preprocess(splitted[k])
        print('words = ' + str(words))
        for z in range(len(words)):
            if(words[z] == 'stay' or words[z] == 'locat' or words[z] == 'place' or words[z] == 'cozi'):
                summ = activity(splitted[k])
                a = (R.r['as.numeric'](summ))
                summm = summm + a[3]
                print('summm = ' + str(summm))
                countt = countt +1
                print('ccount = ' + str(countt))
                break
    if(countt !=0):
        arr2[i] = summm/countt
    print('arr = ' + str(arr2[i]))
    
    
arr3 = [0]*100 
review = dataset.iloc[:,[13]].values
for i in range(len(review)):
    splitted = review[i][0].split(", '")
    print('split = ' + str(splitted))
    summm = 0
    countt = 0
    for k in range(len(splitted)):
        words = preprocess(splitted[k])
        print('words = ' + str(words))
        for z in range(len(words)):
            if(words[z] == 'staff' or words[z] == 'friend' or words[z] == 'host'):
                summ = activity(splitted[k])
                a = (R.r['as.numeric'](summ))
                summm = summm + a[3]
                print('summm = ' + str(summm))
                countt = countt +1
                print('ccount = ' + str(countt))
                break
    if(countt !=0):
        arr3[i] = summm/countt
    print('arr = ' + str(arr3[i]))
    
  
d = dict({'arr' : arr, 'arr2' : arr2, 'arr3' : arr3,'No of Review' : dataset.iloc[:,[4]].values, 'Response rate' : dataset.iloc[:,[8]].values,'Host no of reviews' : dataset.iloc[:,[11]].values})
df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in d.items() ]))  
            
        

    
    
    
