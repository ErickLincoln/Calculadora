import math

def countdown(n):
    if n <= 0:
        print('lançar!')   
    else:
        print(n)
        countdown(n-1)

count(15)