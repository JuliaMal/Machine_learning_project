# flask for web app.
from flask import Flask, render_template, Response, request, redirect, url_for, jsonify

import json

# numpy for numerical work.
import numpy as np

# read a csv file and organise our data
import pandas as pd

#from sklearn import function to split the dataset into train & test sets
from sklearn.model_selection import train_test_split

# Neural networks.
import tensorflow.keras as kr

# Read the powerproduction.csv from a file
df = pd.read_csv('powerproduction.csv')

# removing all rows where the power data is not maintained (equals 0.0)
df = df[df['power'] !=0]

# Split dataset into input (x) and output (y).
x = df.iloc[:, 0].values 
y = df.iloc[:, 1].values

# splitting the dataset into train & test sets (70% train & 30% test)
# to have rows assigned to the train and test sets randomly random_state is used
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

# Create a neural network with 3 layers
model_kr = kr.models.Sequential()
model_kr.add(kr.layers.Dense(50, input_shape=(1,), activation='sigmoid', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
model_kr.add(kr.layers.Dense(50, input_shape=(50,), activation='sigmoid', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
model_kr.add(kr.layers.Dense(1, activation='linear', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
model_kr.compile(kr.optimizers.Adam(lr=0.001), loss='mean_squared_error')

## Train the neural network on our training data.
model_kr.fit(x_train, y_train, epochs=500, batch_size=20)

# Create a new web app.
app = Flask(__name__, template_folder="templates")

# Add root route.
@app.route("/")
def home():
  return render_template('index.html')

@app.route('/prediction')
def predict_power():
  # reads the user input value
    a = request.args.get('a', 0, type=float)
  # predict the power input for given argument a
    predicted_power = model_kr.predict([a])
  # transforms value to the list
    b = predicted_power.tolist()
  # returns the result
    return jsonify(result=b)

if __name__ == '__main__':
    app.run()