import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_BOT_TOKEN = 'xoxb-your-slack-bot-token'
CHANNEL_ID = 'C06SBHMQU8G'

client = WebClient(token=SLACK_BOT_TOKEN)

def searchMessages(channelId, searchQuery):
    userIds = set()
    cursor = None
    while True:
        try:
            if cursor:
                response = client.search_messages(channel=channelId, query=searchQuery, sort="timestamp", cursor=cursor, count=1000)
            else:
                response = client.search_messages(channel=channelId, query=searchQuery, sort="timestamp", count=1000)
            
            if response['ok']:
                for message in response['messages']['matches']:
                    userIds.add(message['user'])
                
                if 'response_metadata' in response and 'next_cursor' in response['response_metadata']:
                    cursor = response['response_metadata']['next_cursor']
                else:
                    break
            else:
                print(f"Error: {response['error']}")
                break
        except SlackApiError as e:
            print(f"Error fetching messages: {e.response['error']}")
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
    searchQuery = 'in:#arcade "you\'ve got a arcade session! this session is now approved!"'
    userIds = searchMessages(CHANNEL_ID, searchQuery)
    if userIds:
        saveUserIdsToFile(userIds, 'arcade_session_user_ids.txt')
    else:
        print(f"No user IDs found matching the search query in channel {CHANNEL_ID}.")
