#1 Write a python program to merge two lists.
#input_list1 = input("input_list1: ").split(',')
#input_list2 = input("input_list2: ").split(',')
#merge = input_list1 + input_list2
#print(merge)

#2method
  #  input_list1 = input("input_list1: ").split(',')
  #  input_list2 = input("input_list2: ").split(',')
  #  input_list1.extend(input_list2)
  #  print(input_list1)



#input_list = input("input_list1: ").split(',')
#total_list = [int(num) for num in input_list]
#total_sum = sum(total_list)
#print(total_sum)

#2nd method
#input_list = input("input_list1: ").split(',')
#total_list = [int(num) for num in input_list]
#total_sum = 0
#for num in total_list:
 #   total_sum += num
#print(total_sum)


#3 Writea python program to print even and odd numbers seperatly in list.
#input_list = input("input_list1: ").split(',')
#total_list = [int(num) for num in input_list]
#even = []
#odd = []
#for num in total_list:
 #   if num % 2 == 0:
  #      even.append(num) 
   # else:
    #    odd.append(num)
#print(even)
#print(odd)

#2nd method
#input_list = input("input_list1: ").split(',')
#total_list = [int(num) for num in input_list]
#even_num = [num for num in total_list if num % 2 == 0]
#odd_num = [num for num in total_list if num % 2 != 0]
#print(even_num)
#print(odd_num)


#4 Write a python program to delete a element of given index in list.
#input_list = input("input_list1: ").split(',')
#input_index = int(input())
#input_list.pop(input_index)
#print(input_list)



#5 Write a pytho program to delete a element from the list.
#input_list = input("input_list1: ").split(',')
#input_index = input()
#input_list.remove(input_index)
#print(input_list)



#6Write a pythhon program to insert an element at given index location.
#input_list = input("input_list1: ").split(',')
#input_element = int(input("enter the element: "))
#input_index = int(input("enter the index: "))
#input_list.insert(input_index, input_element)
#print(input_list)


#7 Write a python program to check the size of the given two lists are same
#input_list1 = input("input_list1: ").split(',')
#input_list2 = input("input_list1: ").split(',')
#len_input_list1 = len(input_list1)
#len_input_list2 = len(input_list2)
#com_size = len_input_list1 == len_input_list2
#print(com_size)

#2nd method
#input_list1 = input("input_list1: ").split(',')
#input_list2 = input("input_list1: ").split(',')
#len_input_list1 = len(input_list1)
#len_input_list2 = len(input_list2)
#if len_input_list1 == len_input_list2:
#    print("True")
#else:
#    print("False")


#8 Write a python function that takes two lists and returns True if they have at least one common member
#input_list1 = input("input_list1: ").split(',')
#input_list2 = input("input_list2: ").split(',')
#list1 = set(input_list1)
#list2 = set(input_list2)
#if list1.intersection(list2):
#    print("True")
#else:
#    print("False")

#2nd method
#input_list1 = input("input_list1: ").split(',')
#input_list2 = input("input_list2: ").split(',')
#list1 = set(input_list1)
#list2 = set(input_list2)
#if any(item in list1 for item in list2):
#    print("True")
#else:
#    print("False")


#8 write a python program to remove a specified column from a given nested list.
#main_list = [[1,2,3], [2,4,5], [1,1,1]]
#item_remove = int(input())
#for list_ in main_list:
 #   del list_[item_remove]
#print(item_remove)
#for list_ in main_list:
#    print(list_)


#9 Write a python program to convert a list of multiple integers into a single integer.
#input_list = input("Enter: ").split(',')
#empty = ""
#for num in input_list:
#    empty += str(num)
#con_int = int(empty)
#print(con_int)


#10 Write a python program to remove duplicates from the list.
#input_list = input("Enter: ").split(',')
#new_list = []
#for item in input_list:
#    if item not in new_list:
#        new_list.append(item)
#print(new_list)

#2nd method
input_list = input("Enter: ").split(',')
new_list = list(set(input_list))
new_list.sort()
print(new_list)


























