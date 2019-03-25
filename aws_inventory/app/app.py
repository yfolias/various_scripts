from flask import Flask, render_template, url_for, request
import subprocess
import boto3

app = Flask(__name__)


# app.config['DEBUG'] = True

@app.route("/")
def index():
    title = "HOME"
    headline = "Home"
    body = "Coming soon"

    return render_template("home.html", headline=headline, title=title, body=body)


@app.route("/ec2")
def ec2():
    title = "EC2"
    headline = "EC2 Instances"
    field1 = "Instance ID"
    field2 = "Name"
    field3 = "Public IP"
    field4 = "Private IP"
    field5 = "VPC Id"
    try:

        client = boto3.client('ec2')
        response = client.describe_instances()
        ec2_ids = []
        for reservation in response["Reservations"]:
            for i in reservation["Instances"]:
                ec2_ids.append(i['InstanceId'])
        ec2_prv = []
        for reservation in response["Reservations"]:
            for i in reservation["Instances"]:
                ec2_prv.append(i['PrivateIpAddress'])

        for reservation in response["Reservations"]:
            for i in reservation["Instances"]:
                ec2_prv.append(i['PrivateIpAddress'])

        ec2_pbl = []
        for reservation in response["Reservations"]:
            for i in reservation["Instances"]:
                ec2_pbl.append(i['PublicIpAddress'])



        inst_num = len(ec2_ids)

    except:
        response = "Unable to connect to EC Service"

    return render_template("ec2.html", headline=headline, inst_num=inst_num , response=response,
                           ec2_pbl=ec2_pbl, ec2_ids=ec2_ids, ec2_prv=ec2_prv, title=title, field1=field1, field2=field2,
                           field3=field3, field4=field4, field5=field5)


@app.route("/rds")
def rds():
    title = "RDS"
    headline = "RDS databases"
    field1 = "DB Identifier"
    field2 = "Engine"
    field3 = "Region"
    field4 = "VPC"
    field5 = "Status"
    client = boto3.client('rds')
    response = client.describe_db_instances()
    rds_list = []
    for r in response['DBInstances']:
        rds_list.append(r['DBInstanceIdentifier'])

    return render_template("rds.html", headline=headline, body=rds_list, title=title, field1=field1, field2=field2,
                           field3=field3, field4=field4, field5=field5)


@app.route("/iam")
def iam():
    title = "IAM"
    headline = "AWS Identity and Access Management"
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_users')
    user_list = []
    for page in paginator.paginate():
        for user in page['Users']:
            user_list.append(user['UserName'])

    paginator = iam.get_paginator('list_groups')
    group_list = []
    for page in paginator.paginate():
        for group in page['Groups']:
            group_list.append(group['GroupName'])
    user_num = len(user_list)
    group_num = len(group_list)
    return render_template("iam.html", headline=headline , title=title, users=user_num , groups=group_num )


@app.route("/lb")
def lb():
    title = "Load Balancers"
    headline = "Elastic Load Balancing"
    field1 = "Name"
    field2 = "Instances"
    field3 = "Health Check"
    field4 = "Listenners"
    field5 = "Creation date"
    lb_list = []
    try:
        client = boto3.client('elb')
        load = client.describe_load_balancers()
        for lb in load['LoadBalancerDescriptions']:
            lb_list.append(lb['LoadBalancerName'])
    except:
        lb_list = "Error"
    return render_template("elb.html", headline=headline, title=title, body=lb_list, field1=field1, field2=field2,
                           field3=field3, field4=field4, field5=field5)


@app.route("/vpc")
def vpc():
    title = "VPC"
    headline = "AWS Virtual Private Cloud"
    field1 = "Name"
    field2 = "VPC Id"
    field3 = "IPv4 CIDR"
    field4 = "Main Network ACL"
    field5 = "State"

    return render_template("vpc.html", headline=headline, title=title, field1=field1, field2=field2, field3=field3,
                           field4=field4, field5=field5)


@app.route("/sec_groups")
def sec_groups():
    title = "SECURITY GROUPS"
    headline = "AWS security groups "
    field1 = "Group ID"
    field2 = "Group Name"
    field3 = "Owner"
    field4 = "Description"
    field5 = "VPC Id"
    body = "Coming soon"

    return render_template("sec_groups.html", headline=headline, body=body , title=title, field1=field1, field2=field2, field3=field3,
                           field4=field4, field5=field5)


@app.route('/<path:path>')
def catch_all(path):
    headline = "The page you are looking for does not exist"
    title = "404"
    return render_template("layout.html", headline=headline, title=title)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
