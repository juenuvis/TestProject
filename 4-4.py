# numbers = ['1', '2', '3', '8', '7', '28']
# number = numbers[:3]
# # print(number)
# print("The first three items in the list are: " \ + str(number))
pizzas = ['Hawaii', 'ham', 'fruit', 'durian', 'pork']
friend_pizzas = pizzas[:]
pizzas.append('mutton')
print("1: " + str(pizzas))
print("2: " + str(friend_pizzas))                                                                                                                               
print("My favorite pizzas are:") 
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)



