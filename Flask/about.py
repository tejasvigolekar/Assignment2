from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return"""
<h1>WCL TO FLASK APP</h1>
<p>This is the home page</p>
"""
@app.route('/about')
def about():
    return"""
    <h1>Wct the about app</h1>
    <p>This is about pagess</p>
"""
@app.route('/contact')
def contact():
    return"""
    <h1>Contact us</h1>
    <p>Email:info@example.com</p>
    """
if __name__=="__main__":
    app.run(debug=True,port=5001)