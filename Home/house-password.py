import re
def checkio(data):
    low = False
    up = False
    ints = False
    if(len(data)<10): return False
    if(re.match("[a-zA-Z0-9]+", data)):
        for i in data:
            if(i.isdigit()): ints = True
            if(i.islower()): low = True
            if(i.isupper()): up = True
    if(low and up and ints):
        return True
    else: return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
