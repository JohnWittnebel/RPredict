import json
import requests

api_token = open("token.txt", "r").read().split('\n')[0]
api_url_base = 'https://americas.api.riotgames.com/lol/match/v5/matches/NA1_4784149077'
api_url_base_summoner = 'https://na1.api.riotgames.com/lol//lol/match/v5/matches/by-puuid/hfRMj8voc1BVjg0mfdVzUwp9cJLLLqq1lh-jDGHepTVkooBcg0u2O0AD9MBVjdHllmFNS7seIV64RA/ids'
api_url_base_summoner = '/lol/league/v4/entries/by-summoner/{encryptedSummonerId}'

headers = {'Content-Type': 'application/json',
           'X-Riot-Token': api_token}


def get_request():
  
    api_url = '{0}'.format(api_url_base)
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print(response)
        return None



def parse_team_data(api_response):
    team1 = []
    team2 = []
    for player in api_response["info"]["participants"]:
        playerData = [player["teamPosition"], player["championName"], player["summoner1Id"], player["summoner2Id"], player["puuid"]]
        if player["teamId"] == 100:
            team1.append(playerData)
        else:
            team2.append(playerData)
    return [team1, team2]


jsonResults = get_request()
teams = parse_team_data(jsonResults)
print(teams[0][4])

print(jsonResults["info"]["gameVersion"])

