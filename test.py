from flask import *

# initialize flask
app=Flask(__name__)

# create a route/ end point
@app.route("/api/home")
def home():
    return jsonify({"Message":"Welcome to home Api"})

# create a route for products
@app.route("/api/products")
def products():
    return jsonify({"Message":"Welcome to products Api"})

# creating a route for services
@app.route("/api/services")
def services():
    return jsonify({"Message":"Welcome to Our Services API"})

# post method
@app.route("/api/calc",methods=["POST"])
def calc():
    # request user input
    num1=request.form["num1"]
    num2=request.form["num2"]

    sum=int(num1)+int(num2)
    return jsonify({"Answer":sum})
    
@app.route("/api/multiply",methods=["POST"])
def multiply():
    value1=request.form["value1"]
    value2=request.form["value2"]

    ans=int(value1)*int(value2)
    return jsonify({"Answer":ans})
  

# creating another route
@app.route("/api/message")
def message():
    return jsonify({"message":"Welcome to Modcom"})


@app.route("/api/weather")
def weather():
    return jsonify({"Message":"It's Raining"})



app.run(debug=True)