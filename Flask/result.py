from flask import Flask
app=Flask(__name__)
@app.route('/')
def result():
    sub1=88
    sub2=78
    sub3=90
    sub4=87
    sub5=99
    total=sub1+sub2+sub3+sub4+sub5
    percentange=total/5
    return f"""
<h1>Student Result</h1>
<hr>
sub1:{sub1}<br>
sub2:{sub2}<br>
sub3:{sub3}<br>
sub4:{sub4}<br>
sub5:{sub5}<br>
<b>Total marks:</b>{total}<br><br>
<b>percentage:</b>{percentange:.2f}%
"""
if __name__=="__main__":
 app.run(debug=True)