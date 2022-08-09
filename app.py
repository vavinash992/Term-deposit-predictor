from email import message
from flask import Flask,redirect, request,url_for,render_template
import bz2
import pickle
import _pickle as cPickle

app=Flask(__name__)


from joblib import Parallel, delayed
import joblib
 
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/model/<string:age>/<string:maritalstatus>/<string:education>/<string:balance>/<string:houseloan>/<string:prevloan>/<string:contact>/<string:day>/<string:month>/<string:job>/<string:duration>/<string:cper>/<string:poutcome>")
def model(age,maritalstatus,education,balance,houseloan,prevloan,contact,day,month,job,duration,cper,poutcome):
    data = joblib.load('filename.pkl')
    [k]=data.predict([[float(age),float(job),float(maritalstatus),float(education),float(balance),float(houseloan),float(prevloan),float(contact),float(day),float(month),float(duration),float(cper),float(poutcome)]])
    if k==0.0:
        ke="The person won't take a loan"
    if k==1.0:
        ke="The person will take a loan"
    return render_template("result.html",message=ke)

@app.route("/action",methods=["POST","GET"])
def submit():
    if request.method=="POST":
        age=request.form["age"]
        maritalstatus=request.form["maritalstatus"]
        education=request.form["education"]
        balance=request.form["Balance"]
        houseloan=request.form["loan"]
        prevloan=request.form["prevloan"]
        contact=request.form["contact"]
        day=request.form["day"]
        month=request.form["month"]
        job=request.form["job"]
        duration=request.form["duration"]
        cper=request.form["cper"]
        poutcome=request.form["poutcome"]
    return redirect(url_for("model",age=age,maritalstatus=maritalstatus,education=education,balance=balance,houseloan=houseloan,prevloan=prevloan,
                            contact=contact,day=day,month=month,job=job,duration=duration,cper=cper,poutcome=poutcome))

if __name__ == "__main__":
    app.run(debug=False)