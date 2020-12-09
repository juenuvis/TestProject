names = ['willosn', 'Mao', 'bill', 'Gates']
for i in range(len(names)):
    print("Guests are" + "第" + str(i) + "位" + names[i])
absent_guest = "Mao"
print("缺席:" + absent_guest)
new_guest = "Jiang"
names[2] = new_guest
for i in range(len(names)):
    print(names[i])
new_names = ['hu', 'Kong', 'Deng']
names.insert(0, 'hu')
names.insert(2, 'Deng')
names.append('Kong')
print(names)
print(len(names))
for i in range(len(names) - 2):
    delete_names = names.pop(0)
    print("sorry , " + delete_names + ", you are not invited !")
print(names[0] + ", you are invited !")
print(names[1] + ", you are invited !")

