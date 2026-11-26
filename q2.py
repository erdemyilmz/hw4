def bubble_sort(alist):
    count = 0
    for i in range(len(alist)-1):
        for j in range(len(alist)-1-i):
            count += 1
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                
    return count
