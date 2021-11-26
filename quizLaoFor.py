# n = 2
# for i in range(1, 11, 1):
#     product = n*i
#     print(product,end=' ')
    


# i = 0
# while i <= 10:
#     print(i,end=' ')
#     i += 1
    

# for num in range(-10, 0, 1):
#     print(num, end=' ')

# for i in range(10):
#     print(i)

# for x in  range(6):
    
#              if(not(x ==2 or x==5)):

#                      print(x,end=' ')

# print("\n")

# Python 3: Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        print()
        a, b = b, a+b
    print()
fib(50)