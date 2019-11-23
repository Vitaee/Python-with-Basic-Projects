def sumList(lst):
    total = 0
    while lst != []:
        total = total + lst[0]
        del lst[0]
    return total

lst = [5,10,30,40]
print("Total of list = ", sumList(lst)) 