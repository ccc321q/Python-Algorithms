
def listSum(inList):
    # returns the sum of all values in a list
    if len(inList) == 1:
        return inList[0]
    else:
        return inList[0] + listSum(inList[1:])