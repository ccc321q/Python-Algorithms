
def SelectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
                
        alist[positionOfMax], alist[fillslots] = alist[fillslots], alist[positionOfMax]