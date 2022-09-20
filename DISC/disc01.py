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

