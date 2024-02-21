from flask import Flask,request

app = Flask(__name__)

@app.route("/lms",methods=["POST"])
def home():
    ansd=request.form.get("Name")
    mental=request.form.get("Age")
    return [ansd,mental]
@app.route("/checkusers",methods=["POST"])
def checkusers():
    hsr=request.form.get("Name")
    totalusers=["har","nit","ahk","lms"]
    if hsr in totalusers:
       return "user valid"
    else:
        return "user invalid"
@app.route("/checkvowels",methods=["POST"])   
def checkvowels():
    tcs=request.form.get("vowel")
    vowels=["a","e","i,","o","u"]
    if tcs in vowels:
        return "its an vowel"
    else:
        return "its not an vowel"
@app.route("/checknumbers",methods=["POST"]) 
def checknumbers():
    num=request.form.get("numbers")
    worst=["1","2","3","10"]
    if num in worst:
        return "1"
    else:
        return "0" #this is false value
