import requests

url = 'https://hackclub.slack.com/api/search.modules.messages'

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryAPebTy6O75z0AfpM',
    'Cookie': 'your-cookie-data-here',
    'Origin': 'https://app.slack.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

data = {
    'token': 'your-token-here',
    'module': 'messages',
    'query': 'in:<#C06SBHMQU8G|arcade> you\'ve got a arcade session! this session is now approved!',
    'page': '2',
    'client_reqId': 'your-clientid-here',
    'searchSessionId': 'your-searchid-here',
    'extracts': '1',
    'highlight': '1',
    'maxExtractLen': '200',
    'extraMessageData': '1',
    'noUserProfile': '1',
    'count': '20',
    'fileTitleOnly': 'false',
    'queryRewriteDisabled': 'false',
    'includeFilesShares': '1',
    'searchContext': 'desktop_messages_tab',
    'searchExcludeBots': 'false',
    'searchOnlyMyChannels': 'false',
    'spellCorrection': 'FUZZY_MATCH',
    'searchOnlyTeam': '',
    'facetsResultCount': '5',
    'queryRefinementSuggestionsVersion': '1',
    'recentChannels': 'C06SBHMQU8G',
    'sort': 'timestamp',
    'sortDir': 'asc',
    'maxFilterSuggestions': '10',
    'requestContext': '{"active_cid":"SearchEmpty","recent_filter_in":["C06SBHMQU8G"],"recent_filter_from":[]}',
    'searchTabFilter': 'messages',
    'searchTabSort': 'timestamp',
    '_xReason': 'search-messages-page',
    '_xMode': 'online',
    '_xSonic': 'true',
    '_xAppName': 'client',
}

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    print('Request successful!')
    print('Response:')
    print(response.json())
else:
    print(f'Request failed with status code {response.status_code}')
    print('Response:')
    print(response.text)
