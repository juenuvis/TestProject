# names = ['willosn', 'Mao', 'bill', 'Gates']
# for i in range(len(names)):
#     friend_name = "This is my friend: " + names[i]
#     print(friend_name)
#     Hello_friend = "Hello " + names[i]
#     print("Hello, " + names[i] + "!")
import random
vehicles = ['motorcycle', 'bike', 'car', 'running', 'metro']
# for i in range(len(vehicles)):
#     print("I would like to own a " + vehicles[i])
count = 0
while (count < len(vehicles)):
    i = random.randrange(0, len(vehicles), 1)
    print("I would like to own a " + vehicles[i])
    count += 1
    


