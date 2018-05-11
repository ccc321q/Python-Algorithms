
def BubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                
def BubbleSortShort(alist):
    """Stops sorting when a complete pass was made without swapping a value"""
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum = passnum-1