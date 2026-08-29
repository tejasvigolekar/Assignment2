from flask import Flask
app=Flask(__name__)
@app.route('/')
def clg():
    return """
    <h1>clg detail</h1>
<hr>
<b> clgname:</b>Abc clg of eng<br><br>
<b >address:</b> PUNE  nera by<br><br>
<b> principle:</b>Dr.kishore More<br><br>
<b>Course:</b> Computer science<br><br>
<ul>
<li>BSA</li>
<li>BCS</li>
<li>MCS</li>
</ul>
<b>Contract number</b>1236546987<br><br>
<b>Website:</b>http://127.0.0.1:5000"""
if __name__=="___Main__":
    app.run(debug=True)