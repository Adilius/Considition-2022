import api
import time
import json


import requests
from requests import RequestException

base_api_path = "https://api.considition.com/api/game/"
sess = None

api_key = "c6e53582-7521-4c0d-bde9-08dabb5bc0fc" 
map_name = "Suburbia"
bag_type = 1


class Solution:
    def __init__(self):
        self.mapName = "Suburbia"
        self.recycleRefundChoice = True
        self.bagPrice = 10
        self.refundAmount = 1
        self.bagType = 1
        self.orders = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def main():
    print("Starting game...")

	# Create solution
    solution = json.dumps(Solution(), default=lambda o: o.__dict__)
    #print(f'Solution: {solution}')

    # Submit solution and get response
    response = requests.post(base_api_path + "submit",
                             headers={"x-api-key": api_key}, verify=True, json=json.loads(solution))
    if response.status_code == 200:
        print("Game OK!")
    else:
        print(response.json())


if __name__ == "__main__":
	while True:
		time.sleep(2)
		main()