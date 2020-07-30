import boto3
import pandas as pd
from datetime import datetime

filename = "iam_report" + datetime.now().strftime("%m-%d-%y") + ".csv"

iam = boto3.client('iam')
users = pd.DataFrame(iam.list_users()['Users']).set_index('UserName')

groups_list = []

for user in users.index:
    groups = ''
    userGroups = iam.list_groups_for_user(UserName=user)
    #print("Username: "  + user)
    for groupName in userGroups['Groups']:
        groups += groupName['GroupName'] + ' ; '
    groups_list.append(groups)
users['Groups'] = groups_list
users.to_csv(filename)

simple_report = users[['PasswordLastUsed','Groups']]
simple_report.to_csv('simple_' + filename)