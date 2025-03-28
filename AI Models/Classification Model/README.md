I trained and deployed a Tabular Classification model in Vertex AI studio in Google, using the auto MLOps process.
Based on dataset of CC Transactions both fraudelent and non-fraudulent, the model predicts with 88% accuracy the likelyhood of a transaction being FRAUD/NOT FRAUD.
The dataset was sourced from Kaggle and is a popular dataset used for understanding Tabular Classification type models

The Notebook Jupyter File is a python script that can call the model and send it data for it to predict Fraud/Not Fraud with a certainty.
There is a UI interface in Google Vertex, but I wanted to create some python scripting that would make the call to my deployed endpoint of the model to return a prediction programatically.
Since the Dataset is heavily unbalanced. <1% of Transactions in the dataset are "Fraud", I used the option of AU-PRC (area under the precision-recall curve - it is a calculated metric used to measure model performance and is popularly used with binary classification when using unbalanced data) within MLops to train this model.
Vertex AI randomly selects 80% of your data rows for the training set, 10% for the validation set, and 10% for the test set.

What other things could I do:
I only did one training of the model. And there are opportunities to further experiment with the dataset as Vertex/Mlops provides graphs and info on what it considers high relation fields to then retraion the model and look for a higher percentage of prediction

The dataset:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download
dataset is 284K rows from 2013 CC european transactions contains less than 1% classified fraudulent transations.

