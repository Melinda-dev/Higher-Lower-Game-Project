from game_data import data
import random

# for dictionary in data:
#     item = dictionary
#     # print(item)

game_continue = True


def get_item(data):
    select_item = random.choice(data)
    return select_item


def comparation(item_A, item_B):
    follower_A = item_A['follower_count']
    follower_B = item_B['follower_count']
    if follower_A > follower_B:
        winner = 'A'
    else:
        winner = 'B'
    return winner


score = 0
while True:

    item_A = get_item(data)
    item_B = get_item(data)
    print(f"A = {item_A['name']}")
    print(f"B = {item_B['name']}")
    guessing = input("who will have more followers, do you think: " )
    answer = comparation(item_A, item_B)
    if guessing == answer:
        score += 1
    else:
        print(f"your score is {score}.")
        exit()

