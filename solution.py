import json

class Solution:
    def __init__(self, mapName: str, recycleRefundChoice: bool, bagPrice: int, refundAmount: int, bagType: int):
        self.mapName = mapName
        self.recycleRefundChoice = recycleRefundChoice
        self.bagPrice = bagPrice
        self.refundAmount = refundAmount
        self.bagType = bagType
        self.orders = []

    def addOrder(self, order):
        self.orders.append(order)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
