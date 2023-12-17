# Introduction to Sentiment Analysis in Health care
It aids in drug safety monitoring, market research, and communication between healthcare providers and patients, enabling data-driven decisions for better healthcare.
Sentiment analysis helps in identifying potential adverse reactions or side effects that patients might be experiencing.
Understanding customer sentiments helps pharmaceutical companies to identify areas of improvement in existing medications.
# Objectives:
a) To evaluate the performance of Deep learning models for prediction of sentiment from drug reviews, including LSTM, Bi-LSTM, LSTM+GRU, and BERT focusing on Accuracy, Precision, Recall, and F1-Score as metrics.
b) To Investigate the impact of dataset balancing on sentiment analysis models and compare the models' performance on both imbalanced and by balanced datasets thereby analysing improvements in accuracy.
c) To explore the impact of FastText word embeddings on sentiment analysis models for both imbalanced and balanced drug review datasets.
d) To check the generalazibilty of models by training the Models on One dataset and evaluating it on other dataset
## Steps:
### 1)Data acquisition:
 In this project we have performed the sentiment analysis of drug reviews, in which the datasets were taken from UCI ML and WEBMD repositories.
### 2) Data preprocessing:
 As we know when we collect the data from repositories it may contain unwanted information such punctuations marks, html tags, urls, Stop words, short hand notations, inflections of words etc
#### Text processing simply means cleaning our dataset from the unwanted  data .
How well the data has been cleaned and preprocessed plays a major role in the performance of the model.
#### Data Preprocessing Technique:
Removing HTML tags
Removing URL's
Removing punctuations
Removing stop words
Chat word treatment
Spelling correction
Tokenization
Stemming
Lemmatization.
### Text representation:
Our deep learning  model will not be able to understand the textual data as humans would.
Textual data is converted in numeric form.
It is must that context of the words must be preserved or maintained.
It helps the model to capture the semantic meaning.
#### Techniques:
Label encoding / integer encoding.
One Hot Encoding.
Bag of words.
#### Word Embedding
##### FastText: a library used for generating word embeddings of words.
## Models used for performing Sentiment Analysis
1) LSTM (Long short term memory)
2) Bi-directional LSTM (Bi-directional long short term memory)
3) LSTM+GRU (hybrid of Long short term memory and Gated recurrent unit)
4) BERT (Bidirectional encoders representations from transformers)
## Model evaluation using various Confusion_matrix, classification_report,Auc and Roc curve, Accuracy, loss curve
In this study, we present an overall performance analysis of Deep learning and advanced pre-trained models on the balanced and imbalanced datasets.
In Deep leaning FastText word embedding showed better performance as compared to one-hot feature extraction technique among all the models of Deep leaning.
Among the Deep learning models the Bi-LSTM performed well on both accuracy and validation loss.
Bi-LSTM performed extremely well in terms of both accuracy and validation loss. As compared to the advanced pre-trained models deep learning models have a higher probability of overfitting.
In advanced pre-trained models BERT showed better results. 





 
