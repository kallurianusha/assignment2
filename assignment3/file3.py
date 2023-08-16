# by using concatenation operator:
# list1 = [1,3,5,7]
# list2 = [2,4,6,8]
# list3 = list1 + list2
# print(list3)


#by append function:
# list1 = [10,30,70,90]
# list2 = [20,60,50,80]
# for i in list2:
#     list1.append(i)
# print(list1)


#by list_comprehension :
# list1 = [10,30,70,90]
# list2 = [20,60,50,80]
# lst = [x for i in(list1,list2)for x in i]
# print(lst)


#by extend method:
# lst1 = [10,28,40,58]
# lst2 = [15,56,79,65]
# lst1.extend(lst2)
# print(lst1)

# to find sum of list:
# num = [1,5,9,19,46]
# print(sum(num))

#by using for loop:
# sum = 0
# for number in [1, 2, 3, 4, 5]:
#     sum += number
# print(sum)


# even numbers in a list:
# list = [2,5,10,15,20,30]
# for num in list:
#     if num % 2 == 0:
#         print(num,end=" ")



#by using pass:
# list1 = [2,4,6,64,14]
# for i in list1:
#     if(i % 2 == 0):
#         pass
#     else:
#         print(i, end=" ")


#odd numbers in a list:
#by list comprehension :
# lst =[13,25,32,45]
# num = [num for num in lst if num % 2 == 1]
# print(num)

# lst2 = [11,13,15,17,23]
# for num in lst2:
#     if num % 2 == 0:
#         print(num,end =" ")

#delete element of given index:
# lst =[1,3,6,8,10]
# for i in lst:
#     if i % 2 == 0:
#         lst.remove(i)
# print("i",lst)


#delete element from list:
# lst=[1,4,6,8,15]
# del lst[-1:]
# print(lst)

#by using pop method:
# lst = [10,20,40,70,90]
# print(lst.pop(3))
# print(lst)


# insert element at given location:
# my_list = [20,30,60,70,100]
# my_list.insert(3,200)
# print(my_list)


#insert element at end:
# my_list= ["apple","banana"]
# my_list.append("mango") 
# print(my_list)

# lst = [20,50,60,80]
# lst.insert(len(lst),500)
# print(lst)


# to check size of 2 elements are same or not:
# lst1=int(input("enter the size1:" ))
# lst2=int(input("enter the size2:"))
# new_list1=[]
# new_list2=[]
# for i in range(0,lst1):
#    element1=int(input("enter the element:"+str(i)+":"))
#    new_list1.append(element1)
# print(new_list1)
# for j in range(0,lst2):
#   element2=int(input("enter the element:"+str()+":"))
#   new_list2.append(element2)
# print(new_list2)
# if len(new_list1)==len(new_list2):
#     print("length are equal")
# else:
#     print("length are not equal")