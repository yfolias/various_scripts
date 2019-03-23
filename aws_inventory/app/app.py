from flask import Flask, render_template, url_for, request, redirect
import os
import subprocess

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    headline = "This is the index page"
    return render_template("layout.html", headline=headline)

@app.route("/ec2")
def ec2():
    headline = "This is the EC2 Instances page"
    try:
        who = subprocess.check_output(["whoami && id"], shell=True)
    except:
        who = "Unable to execute command"
	
    try:
    	  details = subprocess.check_output(["ls -la"], shell=True)
    except:
        details = "Unable to execute command"
        
    return render_template("layout.html", headline=headline , body=who, body2=details)

@app.route("/rds")
def rds():
    headline = "This is the rds page"
    return render_template("layout.html", headline=headline)

@app.route("/iam")
def iam():
    headline = "This is the iam page"
    return render_template("layout.html", headline=headline)

@app.route("/lb")
def lb():
    headline = "This is the load balancers page"
    return render_template("layout.html", headline=headline)

@app.route("/vpc")
def vpc():
    headline = "This is the vpc page"
    return render_template("layout.html", headline=headline)

@app.route("/sec_groups")
def sec_groups():
    headline = "This is the security groups page"
    return render_template("layout.html", headline=headline)

if __name__ == '__main__':
    app.run()
