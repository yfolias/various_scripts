from flask import Flask, render_template, url_for, request
import subprocess

app = Flask(__name__)
#app.config['DEBUG'] = True

@app.route("/")
def index():
    title = "HOME"
    headline = "This is the index page"
    try:
        return render_template("layout.html", headline=headline , title=title)
    except TemplateNotFound:
        abort(404)

@app.route("/ec2")
def ec2():
    title = "EC2"
    headline = "This is the EC2 Instances page"
    try:
        who = subprocess.check_output(["whoami && id"], shell=True)
    except:
        who = "Unable to execute command"
	
    try:
    	  details = subprocess.check_output(["ls -la"], shell=True)
    except:
        details = "Unable to execute command"
        
    return render_template("layout.html", headline=headline , body=who, body2=details , title=title)

@app.route("/rds")
def rds():
    title = "RDS"
    headline = "This is the rds page"
    return render_template("layout.html", headline=headline , title=title)

@app.route("/iam")
def iam():
    title = "IAM"
    headline = "This is the iam page"
    return render_template("layout.html", headline=headline , title=title)

@app.route("/lb")
def lb():
    title = "Load Balancers"
    headline = "This is the load balancers page"
    return render_template("layout.html", headline=headline, title=title)

@app.route("/vpc")
def vpc():
    title="VPC"
    headline = "This is the vpc page"
    return render_template("layout.html", headline=headline , title=title)

@app.route("/sec_groups")
def sec_groups():
    title = "SECURITY GROUPS"
    headline = "This is the security groups page"
    return render_template("layout.html", headline=headline, title=title)

@app.route('/<path:path>')
def catch_all(path):
    headline = "The page you are looking for does not exist"
    title = "404"
    return render_template("layout.html", headline=headline, title=title)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
