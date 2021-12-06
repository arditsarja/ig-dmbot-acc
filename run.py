import json
from src import util
from threading import Thread

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

buttons = []

threads = []

for account in accounts:
    if not usernames:
        break
    usernamesForAccountList = list()
    for i in range(usernamesForAccount):
        if not usernames:
            break
        usernamesForAccountList.append(usernames.pop())
    # util.send_messages(account, usernamesForAccountList)

    # eshte multithreading por nuk me pelqen
    t = Thread(target=util.send_messages, args=(account, usernamesForAccountList,))  # get number for place in list `buttons`
    threads.append(t)
    buttons.append(False)  # create place

for t in threads:
    print(t.name)
    t.start()


for t in threads:
    print(t.name)
    t.join()
