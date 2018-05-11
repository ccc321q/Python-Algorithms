

convertString = "0123456789ABCDEF"

def toStr(n ,base):
    # converts integer to string in base 2 to 16
    if n < base:
        return convertString[n]
    else:
        return toStr(n / base, base) + convertString[n % base]