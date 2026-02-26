from flask import *

import pymysql

# initialize the app
app=Flask(__name__)

@app.route("/api/signup",methods=["POST"])
def signup():
    # request user inputs
    username=request.form["username"]
    email=request.form["email"]
    password=request.form["password"]
    phone=request.form["phone"]

    #  create a connection to mysql
    connection=pymysql.connect(host="localhost",user="root",password="",database="paa_sokogarden_kamal")

    # create a cursor
    cursor=connection.cursor()

    # sql statement to insert the users
    sql="insert into users(username,email,password,phone)values(%s,%s,%s,%s)"

    # prepare data
    data=(username,email,password,phone)

    # execute or run
    cursor.execute(sql,data)

    # commit or save
    connection.commit()

    # Return a response to a user
    return jsonify({"Message":"Thank You for joining"})

# create a signin api
# create the route
@app.route("/api/signin",methods=["POST"])
def signin():
    # request user input
    email=request.form["email"]
    password=request.form["password"]

    # create connection
    connection=pymysql.connect(host="localhost",user="root",password="",database="paa_sokogarden_kamal")

    # create a cursor
    cursor=connection.cursor(pymysql.cursors.DictCursor)

    # sql statement to select
    sql="select * from users where email=%s and password=%s"

    # prepare the data
    data=(email,password)

    # execute or run
    cursor.execute(sql,data)

    #Response
    if cursor.rowcount==0:
        return jsonify ({"message":"Login Failed"})
    else:
        user=cursor.fetchone()
        user.pop("password",None)
        return jsonify({"message":"Login Success","user":user})

# run the app
app.run(debug=True)