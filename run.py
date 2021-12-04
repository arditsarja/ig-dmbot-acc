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

usernamesForAccount = config["usernamesForAccount"]

if len(accounts) * usernamesForAccount < len(usernames):
    print('Problem pasi kemi ' + (len(accounts)) + ' accounte')
    print('Problem pasi kemi ' + (len(accounts) * usernamesForAccount) + ' username mundesi per ti derguar mesazh')
    print('Problem pasi kemi ' + (len(usernames)) + ' qe duam ti dergojme mesazh')
    print(
        'Problem pasi kemi ' + (len(usernames) - (len(accounts) * usernamesForAccount)) + ' accounte pa i derguar mesazh')

for account in accounts:
    if not usernames:
        break

    # Auto login
    insta = InstaDM(username=account["username"],
                    password=account["password"], headless=False)

    for i in range(usernamesForAccount):

        if not usernames:
            break

        username = usernames.pop()

        # Send message
        insta.sendMessage(
            user=username, message=random.choice(messages))

    insta.teardown()
