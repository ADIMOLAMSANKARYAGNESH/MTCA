def printSeriesIncreasing(ch,n):
    for i in range(1,n+1,1):
        print(ch*i)
    return None
def printSeriesDecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None
inpCh=input("Enter a character:")
inpNum=int(input("Enter a number:"))
printSeriesIncreasing(inpCh,inpNum)
print('-'*20)
printSeriesDecreasing(inpCh,inpNum)
