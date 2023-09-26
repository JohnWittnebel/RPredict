import json
import requests

api_token = 'RGAPI-1706aa38-5b00-442d-93ab-2f30ba9d09bb'
api_url_base = 'https://na1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5'

headers = {'Content-Type': 'application/json',
           'X-Riot-Token': api_token}


def get_account_info():
  
    api_url = '{0}'.format(api_url_base)

    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        print("yay")
        return json.loads(response.content.decode('utf-8'))
    else:
        print("boo")
        return None


get_account_info()
