# Drug Review Sentiment Analysis Using Various Deep Learning Architectures
## Project Overview
The Drug Review Sentiment Analysis project focuses on employing various deep learning architectures to analyze sentiments expressed in drug reviews. In this project i have analyzed the customer feedback or reviews of drug products and have classified them based on the sentiment of the words present in the reviews into Positive, Neutral and Negative.
## Purpose of Project:
1) Customer Feedback Analysis: Sentiment analysis helps businesses analyze customer reviews, feedback surveys, this information can guide product improvements, marketing strategies, and customer service enhancements.
2) Brand Monitoring and Social Media analytics: can use sentiment analysis to analyze social media data, including tweets, posts, and comments, to understand public perception, trends, and sentiment shifts related to their industry, products, or services.
3) By automating the sentiment analysis process, corporations can efficiently gather and process feedback about their products, enabling data-driven decision-making and proactive issue resolution.

# FrameWork
![Project FrameWork](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/blob/main/Images/Frame_Work.drawio%20(1).png)

## Key Features
Utilization of LSTM, Bi-LSTM, LSTM+GRU, and BERT deep learning models for sentiment analysis.
Comparative analysis of model performance to determine the most effective architecture.
Handling of imbalanced datasets through oversampling techniques.
Integration of word embedding techniques such as FastText to preserve sentence context.
Implementation of data preprocessing steps including HTML tag removal, URL removal, punctuation removal, stop word removal, chat word treatment, spelling correction, tokenization, stemming, and lemmatization.
## Datasets
Two datasets were utilized, sourced from Kaggle and the UCI ML repository, containing 162,000 and 360,000 rows respectively. Each dataset includes reviews and corresponding customer satisfaction levels categorized as positive, neutral, or negative.
# Data Acquisition:
Data collected from Kaggle and UCI ML repository.<br>
Dataset1 URL:https://www.kaggle.com/datasets/jessicali9530/kuc-hackathon-winter-2018<br>
Dataset2 URL: https://www.kaggle.com/datasets/rohanharode07/webmd-drug-reviews-dataset
Also available in the Dataset sub-repository of this project.
# Data Preprocessing:
Removal of unwanted information using various techniques.
Techniques used for Data Pre-Processing are
### 1) Removing HTML tags
### 2) Removing URL's
### 3) Removing punctuations
### 4) Removing stop words
### 5) Chat word treatment
### 6) Tokenization
### 7) Stemming
### 8) Lemmatization.
## Below Image Shows Data After Preporcessing and Data Before PreProcessing.
![image](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/d0c352f1-7d6a-4aa9-80e6-a03de341723a)
## Handling imbalanced datasets through oversampling.
Using Oversampling Technique to address class imbalace in the dataset. Class imablance leads to biased results.
<div style="display: flex;">
    <img src="https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/df39367c-ddd0-4244-86b6-09ebbfb1dc90" alt="Data distributio before" style="width: 45%;">
    <img src="https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/2c992805-2cad-4e9d-b96c-1ff6d7a30a23" alt="Data Distibution After" style="width: 45%;">
</div>
Conversion of text into numeric form using word embedding techniques.
# Model Selection:
Choose from LSTM, Bi-LSTM, LSTM+GRU, and BERT architectures based on the context preservation requirement.
Model Training and Evaluation:
Train models on the prepared datasets.
Evaluate model performance using appropriate metrics.
# Objectives
Aid in drug safety monitoring, market research, and healthcare provider-patient communication.
Identify potential adverse reactions and side effects through sentiment analysis.
Identify areas of improvement in existing medications.
Align with Agile Methodology by facilitating data-driven decisions and iterative improvements.
Motivation
Address the issue of substandard or falsified medical products.
Enhance pharmacovigilance systems through automated analysis of user reviews.
Provide personalized care and treatment plans by understanding patient perspectives.
Empower healthcare decision-makers with valuable sentiment analysis data.
## Acknowledgments
Mention any scikit-learn,numpy,pandas,seaborn,matplotlib,nltk,re,tensorflow,keras,string,wordcloud,gensim,FastText, Dataset from UCI ML repository,and Webmd,Blog of <b>colah</b>.
## Contributors
Suhaib mukhtar: Development and planning.
Owais & irfan: Presentations and documentation.
Contact:
suhaibmukhtar2@gmail.com
Provide contact information for support or inquiries.
