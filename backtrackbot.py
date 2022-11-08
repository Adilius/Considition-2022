from main import step
import api
import random
import argparse
import threading

import sys
sys.setrecursionlimit(9001) # OVER NINE THOUSAND recursions!!


DAYS = 31
ORDER_OF_OPERATIONS = list(range(1, 4+DAYS*2+1))
random.shuffle(ORDER_OF_OPERATIONS)
#print(ORDER_OF_OPERATIONS)


counter = 0
counter_max = 100
max_score = -999999

previous_score = -99999
previous_move = 1
stored_bagPrice = 1
stored_refundAmount = 1
stored_orders = [0] * 31

map_name = "Suburbia"
bag_type = 1

# 1 - Increase bag price
# 2 - Reduce bag price
# 3 - Increase deposit 
# 4 - Decrease deposit
# (5,65) - Increase/Decrease buy order for that day

def take_step(bagPrice, refundAmount, orders, previous_score, previous_move, current_oop):

    # Get global variables for terminal run
    global map_name
    global bag_type

    # Count amount of recursive calls
    global counter
    counter += 1

    # If we have run 100 recursive calls and still no increase of score, set current values to stored values
    global counter_max
    global max_score
    global stored_bagPrice
    global stored_refundAmount
    global stored_orders
    if counter > counter_max:
        counter = 0
        counter_max += 10   # Increase tolerance
        bagPrice = stored_bagPrice
        refundAmount = stored_refundAmount
        orders = stored_orders
        print(f'Setting new params')
        take_step(bagPrice=bagPrice, refundAmount=refundAmount, orders=orders, previous_score = max_score, previous_move = previous_move, current_oop = current_oop)


    # Get score with current values
    reward = step(mapName = map_name, bagPrice=bagPrice, bagType=bag_type, refundAmount=refundAmount, orders=orders)

    # If current reward is higher than stored, overwrite stored values
    if reward is not None:
        if reward > max_score:
            counter = 0
            max_score = reward
            stored_bagPrice = bagPrice
            stored_refundAmount = refundAmount
            stored_orders = orders

    #print(f"Counter: {counter}")
    #print(f"Max score: {max_score}")

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
            take_step(bagPrice=bagPrice, refundAmount=refundAmount, orders=orders, previous_score = reward, previous_move = previous_move, current_oop = current_oop)
        elif i == 2:
            if bagPrice == 0:
                continue
            bagPrice -= 1
            previous_move = i
            take_step(bagPrice=bagPrice, refundAmount=refundAmount, orders=orders, previous_score = reward, previous_move = previous_move, current_oop = current_oop)
        elif i == 3:
            refundAmount += 1
            previous_move = i
            take_step(bagPrice=bagPrice, refundAmount=refundAmount, orders=orders, previous_score = reward, previous_move = previous_move, current_oop = current_oop)
        elif i == 4:
            if refundAmount == 0:
                continue
            refundAmount -= 1
            previous_move = i
            take_step(bagPrice=bagPrice, refundAmount=refundAmount,  orders=orders, previous_score = reward, previous_move = previous_move, current_oop = current_oop)
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
                take_step(bagPrice=bagPrice, refundAmount=refundAmount,  orders=orders, previous_score = reward, previous_move = previous_move, current_oop = current_oop)

            # 5,7,9,... INCREASE ORDER
            else:
                day = int(day/2)-1
                orders[day] += 1
                #print(f'INCREASE DAY:{day} {i}')
                previous_move = i
                take_step(bagPrice=bagPrice, refundAmount=refundAmount, orders=orders, previous_score = reward, previous_move = previous_move, current_oop = current_oop)


if __name__ == "__main__":
    current_oop = ORDER_OF_OPERATIONS
    previous_score = -99999
    previous_move = 1

    bagPrice = 1
    refundAmount = 1
    orders = [0] * 31
    #orders = [9, 0, 0, 0, 0, 9, 0, 0, 14, 11, 0, 0, 0, 8, 0, 0, 0, 0, 0, 1, 0, 4, 0, 0, 0, 1, 0, 1, 0, 0, 0]

    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-m",
        action="store",
        required=True,
        type=str,
        help="Map name",
        metavar="<map>",
        dest="map",
    )
    parser.add_argument(
        "-b",
        action="store",
        required=True,
        type=int,
        help="Bag type",
        metavar="<bag>",
        dest="bag",
    )
    args = parser.parse_args()

    map_name = args.map
    bag_type = args.bag

    try:
        t1 = threading.Thread(target=take_step, args=(bagPrice, refundAmount, orders, previous_score, previous_move, current_oop))
        t2 = threading.Thread(target=take_step, args=(bagPrice, refundAmount, orders, previous_score, previous_move, current_oop))
        t3 = threading.Thread(target=take_step, args=(bagPrice, refundAmount, orders, previous_score, previous_move, current_oop))
        t4 = threading.Thread(target=take_step, args=(bagPrice, refundAmount, orders, previous_score, previous_move, current_oop))
        t5 = threading.Thread(target=take_step, args=(bagPrice, refundAmount, orders, previous_score, previous_move, current_oop))

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
    except:
       print("Error: unable to start thread")

    #take_step(bagPrice, refundAmount, orders, previous_score, previous_move, current_oop)