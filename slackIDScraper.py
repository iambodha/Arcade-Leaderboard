import requests
import json
from datetime import datetime

def simulateApiRequest(marker=None, isFirstRequest=False):
    url = "https://edgeapi.slack.com/cache/T0266FRGM/users/list"
    
    params = {
        "fp": "91",
        "_x_num_retries": "0"
    }
    
    headers = {
        "Authority": "edgeapi.slack.com",
        "Method": "POST",
        "Path": "/cache/T0266FRGM/users/list?fp=91&_x_num_retries=0",
        "Scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "text/plain;charset=UTF-8",
        "Cookie": "your-cookie",
        "Origin": "https://app.slack.com",
        "Priority": "u=1, i",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    
    data = {
        "token": "your-token",
        "include_profile_only_users": True,
        "count": 100,
        "channels": ["C06SBHMQU8G"],
        "filter": "people",
        "index": "users_by_display_name",
        "locale": "en-US",
        "present_first": False,
        "fuzz": 1
    }
    
    if not isFirstRequest and marker:
        data["marker"] = marker
    
    try:
        response = requests.post(url, params=params, headers=headers, json=data)
        response.raise_for_status()
        
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"slackApiResponses_{timestamp}.json"
    
    allResponses = []
    marker = None
    
    for i in range(51):
        isFirstRequest = (i == 0)
        responseData = simulateApiRequest(marker, isFirstRequest)
        if responseData:
            allResponses.append(responseData)
            marker = responseData.get("next_marker")
            if not marker:
                break
        else:
            break
    
    output = {
        "responses": allResponses
    }
    
    with open(filename, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"Output saved to {filename}")

if __name__ == "__main__":
    main()
