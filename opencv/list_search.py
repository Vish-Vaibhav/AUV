# list = ["void", "soul", "body", "gold", "silver", "earth", "heaven", "hell", "chaos", "blank"]

# key = input("Enter a key to search from the list: ")
# exist = False
# count = 0

# for i in list:

#     if i == key:
#         exist = True
#         break
#     count+=1

# if exist:
#     print("Key is found at position: ", count)
# else:
#     print("Key is not found.")

def linear_search(list1, key):
    for i in range(len(list1)):
        if list1[i] == key:
            return i
    return -1

my_list = [5, 2, 9, 1, 7, 4, 8]
key = int(input("Enter a key to search: "))

result = linear_search(my_list, key)

if result != -1:
    print("Key found at index:", result)
else:
    print("Key not found in the list")

