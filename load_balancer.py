import boto3
import pandas as pd
from datetime import datetime


def get_elb(filename):
    elb = 'elb'
    data = boto3.client(elb)
    df = pd.DataFrame(data.describe_load_balancers()['LoadBalancerDescriptions']).set_index('LoadBalancerName')
    df.to_csv(elb + filename)


def get_elbv2(filename):
    elb = 'elbv2'
    data = boto3.client(elb)
    df = pd.DataFrame(data.describe_load_balancers()['LoadBalancers']).set_index('LoadBalancerName')
    df.to_csv(elb + filename)


filename = "_report" + datetime.now().strftime("%m-%d-%y") + ".csv"

get_elb(filename)
get_elbv2(filename)
