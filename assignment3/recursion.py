# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return(x*factorial(x-1)) 
    
# num = 6
# my_result = factorial(num)
# print(my_result)


# def fibonacci(n):
#     if n <=1:
#         return n
#     else:
#         return(fibonacci(n-1)+fibonacci(n-2))
# n = 7
# if n<=0:
#     print("invalid input!")
# else:
#     print("fibonacci series:")
# for i in range(n):
#     print(fibonacci(i))

# def sum(n):
#     if n > 0:
#         return (sum(n - 1) + n )
#     else:
#         return 0
# n = 20
# my_result=sum(20)
# print(my_result)


#lamda()
# squares = lambda x: x ** 2
# print(squares(4))


# x = lambda x:x+3
# print(x(5))

# a = lambda x,y:x*y
# print(a(8,9))


#filter()
# def check_even(x):
#     if x % 2 ==0:
#         return True
#     else:
#         return False
# lst=[1,2,3,4,5,6,8,9,10,16]
# list =list(filter(check_even ,lst))
# print(list)


# def filter_vowels(letter):
#     vowels =['a','e','i','o','u']
#     if letter in vowels:
#         return True
#     else:
#         return False

# letters =['a','s','i','e','u']
# vowels =tuple(filter(filter_vowels , letters))
# print(vowels)


# def is_divisible(i):
#     if i % 7 == 0:
#         return True
#     else:
#         return False
    
# nums =[10,28,35,40,63,70,80]
# is_divisible = filter(is_divisible,nums)
# print (list(is_divisible))
