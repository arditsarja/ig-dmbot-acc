import json
import random

from src.instadm import InstaDM

f = open('infos/accounts.json', )
accounts = json.load(f)

f = open('infos/config.json', )
config = json.load(f)

with open('infos/usernames.txt', 'r') as f:
    usernames = [line.strip() for line in f]

with open('infos/messages.txt', 'r') as f:
    messages = [line.strip() for line in f]


def send_messages(account, list):

    print("Sending message from "+account["username"])
    # Auto login
    insta = InstaDM(username=account["username"],
                    password=account["password"], headless=False)

    for i in range(len(list)):

        if not list:
            break

        username = list.pop()

        # Send message
        insta.sendMessage(
            user=username, message=random.choice(messages))

    insta.teardown()


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
    send_messages(account, usernamesForAccountList)
