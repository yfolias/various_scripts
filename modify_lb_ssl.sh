#!/usr/bin/env bash
# Yannis Folias
# Script for updating AWS load balancers' SSL Certificate based on existing one
# Has to get executed after uploading the new SSL certificate

lb_list=( $(aws elb describe-load-balancers | grep -eLoadBalancerName | ssed -e 's/[",]//g' | awk '{print $2}') )

function getCert(){
        lb=$1
        cert="$(aws elb describe-load-balancers --load-balancer-name $lb | grep -eSSLCertificateId | sed -e 's/[",]//g' |  awk '{print $2}')"
}

for lb in ${lb_list[*]}; do
        getCert $lb

        previousCert="arn:aws:iam::xxxxxxxxx:server-certificate/xxxxxxxxxx"
        newCert="arn:aws:iam::xxxxxxxxxxx:server-certificate/xxxxxxxxxxx"

        if [[ "$cert" == "$previousCert" ]];then

                echo "LB: $lb has $cert"
                echo "changing to $newCert"
                aws elb set-load-balancer-listener-ssl-certificate --load-balancer-name $lb --load-balancer-port 443 --ssl-certificate-id $newCert
        fi
done
