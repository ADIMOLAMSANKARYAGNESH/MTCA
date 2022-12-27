lst=[]
lstOdd=[]
lstEven=[]
while(True):
    inpNum=int(input("Enter a value(-1 to end):"))
    if inpNum==-1:
        break
    elif inpNum%2==1:
        lstOdd.append(inpNum)
    elif inpNum%2==0:
        lstEven.append(inpNum)
lst.sort()
print("Odd:",*lstOdd)
print("Min:",min(lstOdd))
print("Max:",max(lstOdd))
print("Avg:",round(sum(lstOdd)/len(lstOdd),1))
print("Even:",*lstEven)
print("Min:",min(lstEven))
print("Max:",max(lstEven))
print("Avg:",round(sum(lstEven)/len(lstEven),1))

        
