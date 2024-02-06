def delete_name(name, age, shoe, de):
    for i in range(0,4):
        if name[i] == de:
            name.pop(i)
            age.pop(i)
            shoe.pop(i)
            list1 = [name, age, shoe]
            return list1
        else:
            continue

names = []
age = []
shoe_size = []
for i in range(0,4):
    names.append(input("Enter the name of {} person: ".format(i+1)))
    age.append(int(input("Enter the age of {} person: ".format(i+1))))
    shoe_size.append(float(input("Enter the shoe size of {} first person: ".format(i+1))))

to_delete = input("Enter the name of person to remove from the list: ")

detail = delete_name(names, age, shoe_size, to_delete)
for i in range(0,3):
    print(detail[0][i],detail[1][i],detail[2][i])