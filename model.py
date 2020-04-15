# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:51:34 2020

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

from gensim import corpora
from gensim.models import LsiModel
from nltk.tokenize import RegexpTokenizer
from gensim.models.coherencemodel import CoherenceModel

dataset = pd.read_csv('california_hotelroom.csv')

host_review = dataset.iloc[:,[13]].values
textt = []
for i in range(len(host_review)):
    splitted = host_review[i][0].split(", '")
    for k in range(len(splitted)):
        textt.append(splitted[k])
        
host_review = textt

tokenizer = RegexpTokenizer(r'\w+')
en_stop = set(stopwords.words('english'))
p_stemmer = PorterStemmer()

texts = []

for i in host_review:
    print('hey')
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    stopped_tokens = [i for i in tokens if not i in en_stop]
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    texts.append(stemmed_tokens)
    
dictionary = corpora.Dictionary(texts)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in texts]



coherence_values = []
model_list = []

start,stop,step=0,12,1

for num_topics in range(start, stop, step):
    model = LsiModel(doc_term_matrix, num_topics=12, id2word = dictionary)
        # generate LSA model
  # train model
   
    model_list.append(model)
    coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
    coherence_values.append(coherencemodel.get_coherence())
    
x = range(start, stop, step)
plt.plot(x, coherence_values)
plt.xlabel("Number of Topics")
plt.ylabel("Coherence score")
plt.legend(("coherence_values"), loc='best')
plt.show()

number_of_topics=3
words=15

model = LsiModel(doc_term_matrix, num_topics=number_of_topics, id2word = dictionary)
topics = model.print_topics(num_topics=number_of_topics, num_words=words)
print(model.print_topics(num_topics=number_of_topics, num_words=words))
