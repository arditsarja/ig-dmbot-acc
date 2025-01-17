import random

from src import InstaDM

with open('infos/messages.txt', 'r') as f:
    messages = [line.strip() for line in f]


def send_messages(account, list, timewait):
    print("Sending message from " + account["username"])
    # Auto login
    insta = InstaDM(username=account["username"],
                    password=account["password"], timewait=timewait, headless=False)

    for i in range(len(list)):

        if not list:
            break

        username = list.pop()

        # Send message
        insta.sendMessage(
            user=username, message=random.choice(messages))

    insta.teardown()


def send_groupmessages(account, list):
    print("Sending message from " + account["username"])
    # Auto login
    # Put headless=True to remove window
    insta = InstaDM(username=account["username"],
                    password=account["password"], headless=False)

    # Send message
    insta.sendGroupMessage(
        users=list, message=random.choice(messages))

    insta.teardown()
