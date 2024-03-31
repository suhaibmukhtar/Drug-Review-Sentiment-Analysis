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
<div style="display: flex;">
    <img src="https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/9af61d98-c929-4809-95f7-adadd79016df" alt="Data count before" style="width: 45%;">
    <img src="https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/ee7fabae-63e9-4f71-a2f0-dbf355ff0dae" alt="Data count After" style="width: 45%;">
</div>

## Text Representation
Our deep learning  model will not be able to understand the textual data as humans would.
Textual data is converted in numeric form.
It is must that context of the words must be preserved or maintained.
It helps the model to capture the semantic meaning.
### Techniques:
Label encoding / integer encoding.
One Hot Encoding.
Bag of words.
#### Word Embedding
**FastText**: a library used for generating word embeddings of words.
1) For this technique we have used the word Embeddings called the FastText, which is improved version of the Glove Word Embeddings and it provide the character embeddings rather than word embeddings.
![word embedding](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/blob/main/Images/OIP.jpg)
   
   
# Model Selection:
As our data is sequential and we know the Recurrent Neural networks and its advance version work well with it.
![lstm](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/blob/main/Images/lstm.png)
## Models used are:
### 1.LSTM
![image](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/16c26e48-d16e-4035-9492-32e8332f9e78)
### 2.Bi-LSTM
![image](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/ed04116c-f7d8-4f29-bc19-5e74b7a3af6c)
### 3.LSTM+GRU
![image](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/c711bc20-c4ff-4fa6-b69d-1594613e72f6)

### 4.BERT architectures based on the context preservation requirement.
Model Training and Evaluation:
Train models on the prepared datasets.
Evaluate model performance using appropriate metrics.

## Results:
Performance of deep learning models using imbalanced dataset.
![image](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/eb9857fd-8718-4025-9032-362fa86c49f1)
Performance of deep learning models using balanced dataset.
![image](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/2634f84f-8ba6-43aa-83a5-75f9e4792c1b)
![image](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/bdcb92c2-f041-4aa9-b046-df4fcae4cbb2)
![image](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/5120ec58-150f-41a6-900a-7274c4af4f60)
![image](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/5830bae9-b96b-42c0-b35a-3bea443dafcc)
# Classification Reports
![image](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/ffce020d-7b2c-4403-baa3-c0a41a521b43)
![image](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/e679ca93-25db-4790-be48-c4070df6f2e7)
![image](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/e177920e-ff2e-460a-a190-c1305af5f1f8)
# Loss accuracy Curve
![image](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/1f72413f-c309-48a5-a887-1fa6a05cbd8f)
![image](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/d01ee6e0-ac5f-4b12-97b8-87560e7ec069)
![image](https://github.com/suhaibmukhtar/Drug-Review-Sentiment-Analysis/assets/82581514/0e30b40c-1e26-4948-a639-a47d9640da7a)

# References
1) Cristóbal Colón-Ruiz, Isabel Segura-Bedmar, Volume 110, (October 2020) Comparing deep learning architectures for sentiment analysis on drug reviews.
2) Sebastian Kula, Rafal Kozik and Michal Choras (2021) Implementation of the BERT-derived architectures to tackle disinformation challenges
3) Ray Oshikawa, Jing Qian, William Yang Wang (2018) A Survey on Natural Language Processing for Fake News Detection
4) BERT-LSTM model for sarcasm detection in code-mixed social media post (10 oct 2022)
5) Rajnish Pandey& Jyoti Prakash Singh : Journal of Intelligent Information Systems 
6) Sebastian Kula, Rafal Kozik and Michal Choras (2021) Implementation of the BERT-derived architectures Tackle disinformation challenges.
7) Shin J, Jian L, Driscoll K, Bar F (2018) The diffusion of misinformation on social media Temporal pattern, message and source.
8) Chen W, Zhang Y, Yeo CK, Lau CT, Sung Lee B (2018) Unsupervised rumor detection based on users' behaviors using neural networks.
9) Vinodhini Gopalakrishnan, Chandrasekaran Ramaswamy, Volume 15, Issue 4, (August 2017), Patient opinion mining to analyze drugs satisfaction using supervised learning.





# Objectives
Aid in drug safety monitoring, market research, and healthcare provider-patient communication.<br>
Identify potential adverse reactions and side effects through sentiment analysis.<br>
Identify areas of improvement in existing medications.<br>
Align with Agile Methodology by facilitating data-driven decisions and iterative improvements.<br>
## Motivation
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
suhaibmukhtar.io.github.com
