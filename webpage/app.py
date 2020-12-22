# flask for web app.
#import flask as fl
from flask import Flask, request
# numpy for numerical work.
import numpy as np

# Create a new web app.
app = Flask(__name__)

# Add root route.
@app.route("/")
def index():
  return render_template('index.html')

# Add uniform route.
@app.route('/api/uniform')
def uniform():
  return {"value": np.random.uniform()}

# Add normal route.
@app.route('/api/normal')
def normal():
  return {"value": np.random.normal()}

# Add other route.
@app.route('/api/prediction')
def prediction():
  x = 3
  y = x + 2
  return {"value": y}

# Reading input
@app.route('/api/speed')
def windspeed():
    x = 5
    return {"value": x}

@app.route('/get-speed', methods=['GET', 'POST'])
def foo():
    bar = request.form['wind']
    return {value: bar}

if __name__ == '__main__':
    app.run()