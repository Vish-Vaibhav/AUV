def second_max(list1):
    for i in range(len(list1)):
        j = i + 1
        for j in range(len(list1)):
            if list1[i] < list1[j]:
                temp = list1[j]
                list1[j] = list1[i]
                list1[i] = temp
            else:
                continue

    return list1

n = int(input("Enter the numbers of elements for the list: "))
my_list = []
for i in range(n):
    num = int(input())
    my_list.append(num)

print(my_list)
my_list = second_max(my_list)
print(my_list[1])

