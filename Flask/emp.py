from flask import Flask
app=Flask(__name__)
@app.route('/employee/<int:emp_id>/<name>/<departement>')
def employee(emp_id,name,departement):
    return f"""
<h1>Employee profile</h1>
<hr>
<b>Employee id:</b>{emp_id}<br><br>
<b>Name:</b>{name}<br><br>
<b>Departement:</b>{departement}
"""
if __name__=="__main__":
    app.run(debug=True,port=5003)