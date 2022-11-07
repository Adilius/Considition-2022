from solver import Solver
import api
import time
import json
import requests

api_key = "c6e53582-7521-4c0d-bde9-08dabb5bc0fc"

# "Suburbia" "Fancyville"
# "Farmville" "Mountana Ville" "Pleasure Ville" "Scy Scrape City"
map_name = "Suburbia"

# 1 2 3 4 5
bag_type = 1


def main():
    print("Starting game...")

    # Get map info
    map_info = api.map_info(api_key, map_name)
    api.print_map_info(map_info)

    # Create solution
    solver = Solver(game_info=map_info)
    solution = solver.Solve(bag_type)
    print(f"Solution: {solution.toJSON()}")

    # Submit solution and get response
    submit_game_response = api.submit_game(api_key, solution)
    api.print_submit_game(submit_game_response)

    print("Ending game...")


def step(
    mapName="Suburbia",
    recycleRefundChoice=True,
    bagPrice=10,
    refundAmount=1,
    bagType=1,
    orders=[
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    ],
):
    # Create solution
    solution = {
        "mapName":mapName,
        "recycleRefundChoice":recycleRefundChoice,
        "bagPrice":bagPrice,
        "refundAmount":refundAmount,
        "bagType":bagType,
        "orders":orders
    }
    solution = json.dumps(solution)
    print(solution)

     # Submit solution and get response
    response = requests.post("https://api.considition.com/api/game/" + "submit",
                             headers={"x-api-key": api_key}, verify=True, json=json.loads(solution))
    if response.status_code == 200:
        #print("Game OK!")
        print("Score:", response.json()["score"])
        return int(response.json()["score"])
    else:
        print(response.json())


if __name__ == "__main__":
    step()