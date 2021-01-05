# flask for web app.
#import flask as fl
from flask import Flask, render_template, Response, request, redirect, url_for, jsonify
# numpy for numerical work.
import numpy as np

# Create a new web app.
app = Flask(__name__, template_folder="templates")

# Add root route.
@app.route("/")
def home():
  return render_template('index.html')

@app.route('/numbers')
def add_numbers():
    #result = 0
    a = request.args.get('a', 0, type=int)
    # b = request.args.get('b', 0, type=int)
    #y = a + 2
    #result = a + a
    #return jsonify(result = a * a)
    print(a*a)
    y = a+7
    return jsonify(result=y)

#background process happening without any refreshing
#@app.route('/api/normal')
#def normal():
  #return {"value": np.random.normal()}

if __name__ == '__main__':
    app.run()