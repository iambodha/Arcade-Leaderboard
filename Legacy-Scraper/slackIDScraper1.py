import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slackBotToken = 'xoxb-your-slack-bot-token'

client = WebClient(token=slackBotToken)

def getAllUserIds():
    try:
        userIds = []
        response = client.users_list()
        if response['ok']:
            for member in response['members']:
                userIds.append(member['id'])
        else:
            print("Error: Unable to fetch users list")
        return userIds
    except SlackApiError as e:
        print(f"Error fetching users: {e.response['error']}")
        return []

def saveUserIdsToFile(userIds, filePath):
    try:
        with open(filePath, 'w') as file:
            for userId in userIds:
                file.write(f"{userId}\n")
        print(f"User IDs have been saved to {filePath}")
    except Exception as e:
        print(f"Error saving user IDs to file: {e}")

if __name__ == "__main__":
    userIds = getAllUserIds()
    if userIds:
        saveUserIdsToFile(userIds, 'user_ids.txt')
