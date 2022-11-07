from main import step
import api
import random

DAYS = 31
ORDER_OF_OPERATIONS = list(range(1, 4+DAYS*2+1))
random.shuffle(ORDER_OF_OPERATIONS)
print(ORDER_OF_OPERATIONS)

# 1 - Increase bag price
# 2 - Reduce bag price
# 3 - Increase deposit 
# 4 - Decrease deposit
# (5,65) - Increase/Decrease buy order for that day

def take_step(bagPrice, refundAmount, bagType, orders, previous_score, previous_move, current_oop):

    reward = step(bagPrice=bagPrice, refundAmount=refundAmount, bagType=bagType, orders=orders)

    # If game is invalid
    if reward is None:
        return
    
    # If lower reward score than previous run
    if reward <= previous_score:
        return

    # Prioritize last reward-increasing move
    current_oop.insert(0, current_oop.pop(current_oop.index(previous_move)))

    # Artificial Intelligence
    for i in current_oop:
        if i == 1:
            bagPrice += 1
            previous_move = i
            take_step(bagPrice=bagPrice, refundAmount=refundAmount, bagType=bagType, orders=orders, previous_score = reward, previous_move = previous_move, current_oop = current_oop)
        elif i == 2:
            if bagPrice == 0:
                continue
            bagPrice -= 1
            previous_move = i
            take_step(bagPrice=bagPrice, refundAmount=refundAmount, bagType=bagType, orders=orders, previous_score = reward, previous_move = previous_move, current_oop = current_oop)
        elif i == 3:
            refundAmount += 1
            previous_move = i
            take_step(bagPrice=bagPrice, refundAmount=refundAmount, bagType=bagType, orders=orders, previous_score = reward, previous_move = previous_move, current_oop = current_oop)
        elif i == 4:
            if refundAmount == 0:
                continue
            refundAmount -= 1
            previous_move = i
            take_step(bagPrice=bagPrice, refundAmount=refundAmount, bagType=bagType, orders=orders, previous_score = reward, previous_move = previous_move, current_oop = current_oop)
        else:
            day = (i-4) # Remove the length which first 4 orders add to OOP
            # 6,8,10,.... REDUCE ORDER
            if (day % 2) == 0:
                day = int(day/2)-1
                #print(f'REDUCE DAY:{day} {i}')
                if orders[day] == 0:
                    continue
                orders[day] += -1
                previous_move = i
                take_step(bagPrice=bagPrice, refundAmount=refundAmount, bagType=bagType, orders=orders, previous_score = reward, previous_move = previous_move, current_oop = current_oop)

            # 5,7,9,... INCREASE ORDER
            else:
                day = int(day/2)-1
                orders[day] += 1
                #print(f'INCREASE DAY:{day} {i}')
                previous_move = i
                take_step(bagPrice=bagPrice, refundAmount=refundAmount, bagType=bagType, orders=orders, previous_score = reward, previous_move = previous_move, current_oop = current_oop)


if __name__ == "__main__":
    current_oop = ORDER_OF_OPERATIONS
    previous_score = -99999
    previous_move = 1

    bagPrice = 1
    refundAmount = 2
    bagType = 2
    orders = [0] * 31
    orders = [9, 0, 0, 0, 0, 9, 0, 0, 14, 11, 0, 0, 0, 8, 0, 0, 0, 0, 0, 1, 0, 4, 0, 0, 0, 1, 0, 1, 0, 0, 0]
    take_step(bagPrice, refundAmount, bagType, orders, previous_score, previous_move, current_oop)