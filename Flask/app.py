from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
 return "<h1>Hello Flask</h1>"
app = Flask(__name__)
@app.route('/about')
def home():
 return "<h1>about page</h1>"
app = Flask(__name__)
@app.route('/contact')
def home():
 return "<h1>about contact</h1>"
if __name__ == "__main__":
 
  app.run(debug=True,port=5001)