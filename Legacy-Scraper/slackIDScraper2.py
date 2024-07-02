import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slackBotToken = 'xoxb-your-slack-bot-token'
channelId = 'C06SBHMQU8G'

client = WebClient(token=slackBotToken)

def getAllUserIdsFromChannel(channelId):
    userIds = set()
    cursor = None
    while True:
        try:
            if cursor:
                response = client.conversations_members(channel=channelId, cursor=cursor, limit=1000)
            else:
                response = client.conversations_members(channel=channelId, limit=1000)
            
            if response['ok']:
                userIds.update(response['members'])
                
                if 'response_metadata' in response and 'next_cursor' in response['response_metadata']:
                    cursor = response['response_metadata']['next_cursor']
                    if not cursor:
                        break
                else:
                    break
            else:
                print("Error: Unable to fetch members")
                break
        except SlackApiError as e:
            print(f"Error fetching members: {e.response['error']}")
            break
    return list(userIds)

def saveUserIdsToFile(userIds, filePath):
    try:
        with open(filePath, 'w') as file:
            for userId in userIds:
                file.write(f"{userId}\n")
        print(f"User IDs have been saved to {filePath}")
    except Exception as e:
        print(f"Error saving user IDs to file: {e}")

if __name__ == "__main__":
    userIds = getAllUserIdsFromChannel(channelId)
    if userIds:
        print(f"Total members found: {len(userIds)}")
        saveUserIdsToFile(userIds, 'arcadeUserIds.txt')
    else:
        print(f"No user IDs found in channel {channelId}.")
