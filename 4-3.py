# numbers = []
# for i in range(1,1000001):
#     number = i
#     numbers.append(number)
# # print(numbers)
# print(sum(numbers))

# 4-7
# odd_numbers = []
# for i in range(1,20,2):
#     odd_numbers.append(i)
# print(odd_numbers)

#4-7 multiple_number

# multiple_numbers = []
# for i in range(3,31):
#     if i % 3 == 0:
#         # print(i)
#         multiple_numbers.append(i)
# print(multiple_numbers)
numbers = []
for i in range(1, 11):
    # print(i)
    number = i ** 3
    numbers.append(number)
print(numbers)
for number in numbers:
    print(number)