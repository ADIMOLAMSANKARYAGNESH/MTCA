string='''Practice problems for
List Comprehension in Python.'''
ans=[]
for i in string:
    if i == ' ':
        ans.append(i)
print(len(ans))
print(string.count(' '))



