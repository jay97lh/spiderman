def insertion_sort(list):
    for i in range(1, len(list)):
        e = list[i]
        x = 0
        for j in range(i, 0, -1):
            if list[j-1] > e:
                list[j] = list[j-1]
            x = j
        list[x] = e
