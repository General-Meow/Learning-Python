hello = 'hello text'
print(hello)
hello = "hello again"
print(hello)

thisIsaList = ['a', 'list', 'of', 'values']
print('this is the list', thisIsaList)

anotherList = []
anotherList.append('a')
anotherList.append('b')
anotherList.insert(0, 'c')
print('another list created using the []', anotherList)

for item in anotherList:
    print('a value in list during a for loop: ', item)

aTuple = (1,2,3,)
print('a tuple looks like this', aTuple, type(aTuple))
print('most collections/data structures have the count method that count the amount of occurances of a value...', aTuple.count(1))

aSet = {1, 2, 3, 4, 5}
print('Sets are tricky as they look almost like a dict', aSet, type(aSet))

print('you can convert sets into lists by using the list() BIF', list(aSet), type(list(aSet)))

aDict = { 'myKey': 'myValue', 'akey': 'aValue'}
print("Dicts are Maps that look like json", aDict, type(aDict))


