import operator

from solution import Solution


class Solver:
    bagType_price = [1.7, 1.75, 6, 25, 200]
    bagType_co2_production = [5, 7, 3, 6, 20]
    bagType_co2_transport = [50, 40, 60, 70, 100]

    def __init__(self, game_info):
        self.mapName = game_info["mapName"]
        self.days = 31 if game_info["mapName"] == "Suburbia" or game_info["mapName"] == "Fancyville" else 365
        self.population = game_info["population"]
        self.companyBudget = game_info["companyBudget"]
        self.behavior = game_info["behavior"]

    def Solve(self, bagtype):
        solution = Solution(
            mapName = self.mapName,
            recycleRefundChoice = True,
            bagPrice = 10, 
            refundAmount = 1, 
            bagType = bagtype)

        for _ in range(0, self.days):
            #solution.addOrder(self.wasteMoney(bagtype))
            #solution.addOrder(self.splitMoney(bagtype))
            solution.addOrder(self.holdMoney(bagtype))
        
        return solution


    # Solution 1: "Spend all money day 1"
    def wasteMoney(self, bagtype):
        return int(self.companyBudget / self.bagType_price[bagtype])

    # Solution 2: "Spend equally money every day"
    def splitMoney(self, bagtype):
        return int(self.companyBudget / self.bagType_price[bagtype] / self.days)

    # Solution 3: "Everyone get one bag every day"
    def holdMoney(self, bagtype):
        return int(self.companyBudget / self.bagType_price[bagtype] / self.population / self.days)
