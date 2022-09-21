#Q1: Case Conundrum
def special_case():
    x=10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x

print('WWPD: 12, Actual: '+ str(special_case()))

def just_in_case():
    x=10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x

print('WWPD: 19, Actual: ' + str(just_in_case()))

def case_in_point():
    x=10
    if x > 0:
        x + 2
    if x < 13:
        x + 3
    if x % 2 == 1:
        x + 4
    return x

print('WWPD: 10, Actual: ' + str(case_in_point()))

#Q2: Jacket Weather?
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    if temp < 60 or raining:
        return True
    else:
        return False
    
print(wears_jacket_with_if(90, False), False)
print(wears_jacket_with_if(40, False), True)
print(wears_jacket_with_if(100, True), True)

#Q3:Square So Slow
def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

print('infinite loop')

#Q4: Is Prime?
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n < 2:
        return False
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
    return True

print(is_prime(10), False)
print(is_prime(7), True)
print(is_prime(1), False)



