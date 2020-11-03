

def quick_sort(list):
    if len(list) <=1:
        return list
    else:
        pivot = list[len(list) // 2]
        left = [x for x in list if x < pivot]
        middle = [x for x in list if x == pivot]
        right = [x for x in list if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

sort_me = [8, 5, 3, 9, 7, 4, 1, 2, 6]
print(quick_sort(sort_me))


