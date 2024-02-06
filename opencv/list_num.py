def search_list(list1, key):
    for i in range(len(list1)):
        for j in range(len(list1)):
            if list1[i] + list1[j] == key:
                print("Output: [" + str(i) + "," + str(j) + "]")
                return


my_list = [2, 4 , 5 , 9 , 13]

print(my_list)
target = int(input("Enter the target number: "))

search_list(my_list, target)