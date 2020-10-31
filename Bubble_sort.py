
def bubblesort(list):
    for i in range(len(list) - 1, 0, -1):
        for x in range(i):
            if list[x] > list[x + 1]:
                temp = list[x]
                list[x] = list[x + 1]
                list[x + 1] = temp
    return list

sort_me = [9, 2, 1, 4, 7, 6, 5, 3, 8]

print(bubblesort(sort_me))

