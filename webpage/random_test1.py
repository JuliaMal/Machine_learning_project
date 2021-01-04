# flask for web app.
#import flask as fl
from flask import Flask, request, render_template
# numpy for numerical work.
import numpy as np

# Create a new web app.
app = Flask(__name__, template_folder="templates")

# Add root route.
@app.route("/")
def home():
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
@app.route('/api/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
    #speed = request.form.get('windspeed')
        x = request.form.get['windspeed']
        #x = 15
        #y = x + 2
        #return {"value": y}
        return x

# Reading input
@app.route('/api/speed')
def windspeed():
    x = 5
    return {"value": x}

@app.route('/get-speed', methods=['GET', 'POST'])
def foo():
    bar = request.form['wind']
    y = int(bar) + int(bar)
    #bar = bar + bar
    # bar = float(bar)
    return str(y)

@app.route('/api/predict')
def predict():
  z = 50
  return z 

if __name__ == '__main__':
    app.run()