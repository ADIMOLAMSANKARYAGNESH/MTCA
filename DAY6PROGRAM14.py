string='''
Practice problems for List Com pre hension in Python.
'''
#ans=[]
#wordsList=string.split(' ')
#for i in wordsList:
#    if len(i)<5:
#        ans.append(i)
#print(*ans)


wordsList=string.split(' ')
ans=[i for i in wordsList if len(i.strip('\n'))==8]
print(*ans)
