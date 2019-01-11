def checkio(data):
    new_list = []
    for i in data:
        if data.count(i) > 1:
            new_list.append(i)
    return new_list

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
