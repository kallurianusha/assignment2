#to add a key in dictionary:
# my_dict = {0: 10, 1: 20}
# my_dict.update({2: 30})
# print(my_dict)  


#to check the key already exists or not:
# dict1 ={'books':3,'pens':2,'pencils':5}
# dict_check= 'pencils'
# if dict_check in dict1:
#     print('yes the key already exists')
# else:
#     print('no the key is not found')


#iterate dict by using for loop:
# my_dict = {'name':"anusha", "company":"marolix", "city":"hyderabad"}
# for key,value in my_dict.items():
#     print(key,'=',value)

# squares ={x: x * x for x in range (1,16)}
# print(squares)


#creating dict from string:
# sample_string = "marolix technology"
# my_dict ={}
# for letters in sample_string:
#     my_dict[letters]=my_dict.get(letters,0)+1
# print(my_dict)


#sum all items in dict:
# my_dict={'apple':24,"orange":17,'mangoes':20}
# print(sum(my_dict.values()))

#to combine two dict by adding values for common key:
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3 =dict(d1)
# d3.update(d2)
# for k ,v in d1.items():
#     for x,y in d2.items():
#         if k == x:
#             d3[k]=(v+y)
# print(d3)


#access dict keys elements by index:
# my_dict ={'physics':40,'maths':50,'chemistry':80}
# print(list(my_dict)[0])
# print(list(my_dict)[1])
# print(list(my_dict)[2])     


#remove key from a dict:
# my_dict ={'harshi':23,'anu':26,'radha':28}
# my_dict.pop("anu")
# del my_dict['anu']
# print(my_dict)                        


# merge two dict :
# dict1 ={'apple':2,'banana':4}
# dict2 ={'bat':1,'boll':3}
# dict3 =dict2.copy()
# dict3.update(dict1)
# print(dict3)