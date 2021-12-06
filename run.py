import json
from src import util

f = open('infos/accounts.json', )
accounts = json.load(f)

f = open('infos/config.json', )
config = json.load(f)

with open('infos/usernames.txt', 'r') as f:
    usernames = [line.strip() for line in f]


usernamesForAccount = config["usernamesForAccount"]

capacity = len(accounts) * usernamesForAccount
toSent = len(usernames)

if capacity < toSent:
    print('Problem pasi kemi ' + str(len(accounts)) + ' accounte')
    print('Problem pasi kemi ' + str(len(accounts) * usernamesForAccount) + ' username mundesi per ti derguar mesazh')
    print('Problem pasi kemi ' + str(len(usernames)) + ' qe duam ti dergojme mesazh')
    print('Problem pasi kemi ' + str(
        len(usernames) - (len(accounts) * usernamesForAccount)) + ' username pa i derguar mesazh')
    exit()


for account in accounts:
    if not usernames:
        break
    usernamesForAccountList = list()
    for i in range(usernamesForAccount):
        if not usernames:
            break
        usernamesForAccountList.append(usernames.pop())
    util.send_messages(account, usernamesForAccountList)
