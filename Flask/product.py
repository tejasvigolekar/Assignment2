from flask import Flask
app=Flask(__name__)
@app.route('/product/<p_name>/<int:price>/<category>')
def product(p_name,price,category):
    discount=price*0.10
    subtotal=price-discount
    gst=subtotal*0.18
    final_price=subtotal+gst
    return f"""
<h1>Product information</h1>
<hr>
<b>Product Name:</b>{p_name}<br><br>
<b>Price:</b>{price}<br><br>
<b>Category:</b>{category}
<b>Discount(10%):</b>{gst}<br>
<b>GST(18%):</b>{discount}<br><br>
<h2>Final Price:{final_price:2f}</h2>
"""
if __name__=="__main__":
    app.run(debug=True)