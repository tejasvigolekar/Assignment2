from flask import Flask
app=Flask(__name__)
@app.route('/')
def sal():
    eid=101
    name="ABC"
    depar="IT"
    b_sal=50000
    hra=b_sal*0.20
    da=b_sal*0.12
    ta=b_sal*0.08
    pf=b_sal*0.10
    g_sal=b_sal+hra+da+ta
    n_sal=g_sal-pf
    return f"""
<h1>Emp Slary Slip</h1>
<hr>
eid:{eid}<br><br>
name:{name}<br><br>
depar:{depar}<br><br>
b_sal:{b_sal}<br><br>
hra(20%):{hra}<br><br>
da(12%):{da}<br><br>
ta(8%):{ta}<br><br>
pf(10%):{pf}<br><br>
<b>Gross Salary:</b>{g_sal}<br4><br>
<b>Net Salary:</b>{n_sal}<br><br>
"""
if __name__=="__main__":
 app.run(debug=True, port=5001)

   