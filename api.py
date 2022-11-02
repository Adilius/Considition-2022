import json

import requests
from requests import RequestException

base_api_path = "https://api.considition.com/api/game/"
sess = None


def map_info(api_key, map_name):
    try:
        global sess
        if not sess:
            sess = requests.Session()
        response = sess.get(base_api_path + "mapInfo" + "?MapName=" +
                            map_name, headers={"x-api-key": api_key}, verify=True)  
        if response.status_code == 200:
            map_info = response.json()
            map_info['mapName'] = map_name
            return map_info

        print("Fatal Error: could not start game")
        print(str(response.status_code) + " " +
              response.reason + ": " + response.text)
    except RequestException as e:
        print("Fatal Error: could not start game")
        print("Something went wrong with the request: " + str(e))

def print_map_info(map_info: dict):
    print(f'Map info: {map_info}')
    

def submit_game(api_key, solution):
    try:
        global sess
        if not sess:
            sess = requests.Session()
        response = sess.post(base_api_path + "submit",
                             headers={"x-api-key": api_key}, verify=True, json=json.loads(solution.toJSON()))
        if response.status_code == 200:
            return response.json()

        print("Fatal Error: could not submit game")
        print(str(response.status_code) + " " +
              response.reason + ": " + response.text)
    except RequestException as e:
        print("Fatal Error: could not submit game")
        print("Something went wrong with the request: " + str(e))

def print_submit_game(submit_game_response: dict):
    submit_game_response.pop("weekly", None)
    print("Result: \n",json.dumps(submit_game_response, sort_keys=True, indent=4))

def game_data(game_id: str) -> dict:
    response = requests.get(base_api_path + "get?gameId=" + game_id)
    return response