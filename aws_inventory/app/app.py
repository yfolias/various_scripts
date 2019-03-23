from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>OC Solutions</h1>\n<h3>AWS Inventory</h3>"
@app.route("/ec2")
def ec2():
    return "<h1>OC Solutions</h1>\n<h3>AWS Inventory</h3>"