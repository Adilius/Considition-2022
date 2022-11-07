from main import step

class game_state:
    def __init__(self, bag_price, refund_amount, bag_type, orders, previous_score):
        self.bag_price = bag_price
        self.refund_amount = refund_amount
        self.bag_type = bag_type
        self.orders = orders
        self.previous_score = previous_score

def take_step(bagPrice, refundAmount, bagType, orders, previous_score):
    reward = step(bagPrice=bagPrice, refundAmount=refundAmount, bagType=bagType, orders=orders)
    if reward > previous_score:
        print(bagType)
        step(bagPrice=bagPrice, refundAmount=refundAmount, bagType=bagType, orders=orders)
        print(reward)

# def step
# kolla ifall vi är på målet
# ifall man kan, Ta vänster
# Gå fram
# Ta höger
# return


if __name__ == "__main__":
    previous_score = -99999
    bagPrice, refundAmount, bagType, = (1, 1,1)
    orders = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    take_step(bagPrice, refundAmount, bagType, orders, previous_score)