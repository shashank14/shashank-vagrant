import requests
import json
BASE_URL='http://127.0.0.1:9090/'
# ENDPOINT='cricket/'
ENDPOINT='cricket/api/'

# def get_teams():
#
#     resp = requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())
#
# get_teams()


# def get_team(id):
#
#     resp = requests.get(BASE_URL+ENDPOINT+str(id)+'/')
#     print(resp.status_code)
#     print(resp.json())
#
# get_team(5)

def create_team():

    team = {
    'team_id' : 5,
    'team_name' : 'West Indies',
    'team_captain' : 'sammy',
    }
    resp = requests.post(BASE_URL+ENDPOINT,data=json.dumps(team))
    print(resp.status_code)
    print(resp.json())

create_team()
