# def counting_upper_lower_specialcase(strng):
#     upper_count = 0
#     lower_count = 0
#     specialcase_count =0
#     for char in my_string:
#       if char .isupper():
#         upper_count += 1
#       elif char.islower():
#         lower_count += 1
#       else:
#         specialcase_count +=1
#     print(upper_count )
#     print(lower_count )
#     print(specialcase_count)

# my_string =input("enter input string:")
# counting_upper_lower_specialcase(my_string)



# def sorting_list(n):
#     new_list =[]
#     for num in n:
#         if num not in new_list:
#             new_list.append(num)
#     print(new_list)

# list =[1,2,3,3,3,3,4,5]
# sorting_list (list)


# def is_pangram(string):
#   string = string.lower()
#   for letter in "abcdefghijklmnopqrstuvwxyz":
#     if letter not in string:
#       return False
#   return True

# string = input("enter input string:")
# if is_pangram(string):
#   print("the string is in pangram")
# else:
#   print (" the string is not a pangram ")


# def create_and_print_squares_list():
#     squares=[]
#     for num in range(1 ,10+1 ):
#        squares.append(num*num)
#     print("the list of squares is:",squares)
    
# create_and_print_squares_list ()


# def sum_list(nums):
#     sum = 0
#     for num in nums:
#         sum = sum + num
#     return(sum)
# print(sum_list([8,2,3,0,7]))



# def sum_of_values(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(sum_of_values(1, 2, 3, 4, 5))  