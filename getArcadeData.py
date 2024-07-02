import json
import asyncio
import aiohttp

# Function to fetch data asynchronously
async def fetchData(session, idValue):
    url = f"https://hackhour-9870d80cb898.herokuapp.com/api/stats/{idValue}"
    async with session.get(url) as response:
        if response.status == 200:
            try:
                data = await response.json()
                sessions = data['data']['sessions']
                total = data['data']['total']
                return {
                    "id": idValue,
                    "sessions": sessions,
                    "total": total
                }
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error parsing response for ID {idValue}: {e}")
                return None
        else:
            print(f"Failed to fetch data for ID {idValue}. Status code: {response.status}")
            return None

# Function to extract IDs from arcadeData.json and fetch stats asynchronously
async def extractAndFetchStats(jsonFile, outputFile):
    with open(jsonFile, 'r') as f:
        data = json.load(f)
    
    allUsers = []
    tasks = []
    
    async with aiohttp.ClientSession() as session:
        for response in data.get('responses', []):
            for result in response.get('results', []):
                idValue = result.get('id')
                if idValue:
                    task = asyncio.ensure_future(fetchData(session, idValue))
                    tasks.append(task)
        
        if tasks:
            results = await asyncio.gather(*tasks)
            allUsers = [user for user in results if user]
    
    usersData = {
        "users": allUsers
    }
    
    with open(outputFile, 'w') as out:
        json.dump(usersData, out, indent=4)

async def main():
    await extractAndFetchStats('arcadeData.json', 'allUsersStats.json')

if __name__ == '__main__':
    asyncio.run(main())
