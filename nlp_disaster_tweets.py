# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Обработка данных
import string, nltk, re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Построение Deep Learning моделей
import tensorflow as tf
import tensorflow.keras as k
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D

# Построение ML моделей
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
import xgboost as xgb


# Оценка моделей
from sklearn.metrics import roc_auc_score, confusion_matrix, precision_score, recall_score
from sklearn.model_selection import cross_val_score

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

train.head(3)

test.head(3)

train.isnull().sum()

test.isnull().sum()

train.info()

# Количество примеров, относящихся к каждому классу
sns.countplot(x=train["target"]);

train.describe()

def drop_col(data):
    columns = ["id", "keyword", "location"]
    for col in columns:
        data.drop(columns=col, axis=1, inplace=True)
    return data

train = drop_col(train)
test = drop_col(test)

train.head(3)

test.head(3)

train["len"] = train["text"].apply(len)
test["len"] = test["text"].apply(len)

train.head(5)

train.describe()

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

punc = list(string.punctuation)
stop_word = stopwords.words("english")
Lemmatize = WordNetLemmatizer()

def transform_text(text):
    text = text.lower()
    new_text = " ".join([Lemmatize.lemmatize(word) for word in word_tokenize(text) if ((word not in punc) and (word not in stop_word))])

    new_text = re.sub("[^a-z]", " ", new_text)

    return new_text

train["Cleaning-text"] = train["text"].apply(transform_text)
test["Cleaning-text"] = test["text"].apply(transform_text)

train.head(10)

train["len_after_clean"] = train["Cleaning-text"].apply(len)
test["len_after_clean"] = test["Cleaning-text"].apply(len)

train.head(5)

def drop_extra(data):
    columns = ["text", "len"]
    for col in columns:
        data.drop(columns=col, axis=1, inplace=True)
    return data

train = drop_extra(train)
test = drop_extra(test)

train.head(10)

test.head(5)

X = train["Cleaning-text"]
Y = train["target"]

print(X[0], X[1], X[2], X[3], sep='\n')

X

# Tokenization - Training Data

tokenize = Tokenizer(oov_token="<OOV>")
tokenize.fit_on_texts(X)
word_index = tokenize.word_index

data_sequance = tokenize.texts_to_sequences(X)

# Padding_Sequances
data_padding = pad_sequences(data_sequance, maxlen=150, padding="pre", truncating="pre")

data_sequance[0]

data_padding.shape, Y.value_counts()

input_length = max(len(seq) for seq in data_sequance)

vocabulary_size = len(word_index) + 1

input_length, vocabulary_size

smote = SMOTE()
new_data_padding, new_y = smote.fit_resample(data_padding, Y)

new_y.value_counts()

Y.value_counts()

Y

# label  = to_categorical(new_y, 2)
label  = to_categorical(Y, 2)

label[0:5]

label

TFID = TfidfVectorizer(stop_words="english", max_df=0.8, ngram_range=(1, 2))
new_TFID = TFID.fit_transform(X)
test_x = TFID.transform(test["Cleaning-text"])

# TF_IDF
x_train, x_test, y_train, y_test = train_test_split(new_TFID, Y, train_size=0.8, random_state=42)

# Tokenize
x_train_dl, x_test_dl, y_train_dl, y_test_dl = train_test_split(new_data_padding, new_y, train_size=0.8)

model_xgb = xgb.XGBClassifier()

model_xgb.fit(x_train, y_train)

print(f"The predict Score Train is ==> {model_xgb.score(x_train, y_train)}")
print("%----------------------------------------------------------%")
print(f"The predict Score Test is ==> {model_xgb.score(x_test, y_test)}")

model_xgb_DL = xgb.XGBClassifier()

model_xgb_DL.fit(x_train_dl, y_train_dl)

print(f"The predict Score Train is ==> {model_xgb_DL.score(x_train_dl, y_train_dl)}")
print("%----------------------------------------------------------%")
print(f"The predict Score Test is ==> {model_xgb_DL.score(x_test_dl, y_test_dl)}")

Adaboost = AdaBoostClassifier(n_estimators=200,
                              learning_rate=0.2)


Adaboost.fit(x_train, y_train)

print(f"The predict Score Train is ==> {Adaboost.score(x_train, y_train)}")
print("%----------------------------------------------------------%")
print(f"The predict Score Test is ==> {Adaboost.score(x_test, y_test)}")

Adaboost = AdaBoostClassifier(n_estimators=200,
                              learning_rate=0.2)


Adaboost.fit(x_train_dl, y_train_dl)

print(f"The predict Score Train is ==> {Adaboost.score(x_train_dl, y_train_dl)}")
print("%----------------------------------------------------------%")
print(f"The predict Score Test is ==> {Adaboost.score(x_test_dl, y_test_dl)}")

model_rd = RandomForestClassifier()
model_rd.fit(x_train, y_train)

print(f"The predict Score Train is ==> {model_rd.score(x_train, y_train)}")
print("%----------------------------------------------------------%")
print(f"The predict Score Test is ==> {model_rd.score(x_test, y_test)}")

model_rd_DL = RandomForestClassifier()
model_rd_DL.fit(x_train_dl, y_train_dl)

print(f"The predict Score Train is ==> {model_rd_DL.score(x_train_dl, y_train_dl)}")
print("%----------------------------------------------------------%")
print(f"The predict Score Test is ==> {model_rd_DL.score(x_test_dl, y_test_dl)}")

model = tf.keras.models.Sequential(
    [
        Embedding(vocabulary_size, 100, input_length=150),
        GlobalAveragePooling1D(),
        Dense(24, activation="relu"),
        Dense(1, activation="sigmoid")
    ])
model.compile(optimizer="adam", loss=k.losses.BinaryCrossentropy(), metrics=["accuracy"])
model.summary()

history = model.fit(x_train_dl, y_train_dl, epochs=15,
                    validation_data=(x_test_dl, y_test_dl), verbose=2)

plt.plot(history.history["loss"], label="Loss")
plt.plot(history.history["val_loss"], label="Val_Loss")

plt.xlabel("Epochs")
plt.ylabel("Loss")

plt.title("Loss Vs Epochs")

plt.legend()
plt.grid()

plt.plot(history.history["accuracy"], label="accuracy")
plt.plot(history.history["val_accuracy"], label="val_accuracy")

plt.xlabel("Epochs")
plt.ylabel("Accuracy")

plt.title("Accuracy Vs Epochs")

plt.legend()
plt.grid()
