import sys

sys.stdin =  open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

from collections import defaultdict

# set default value to 0 for int if there's no key
dd = defaultdict(int)

dd[1] = "data"
dd["Name"] = "afnan"
dd['u'] = [1,2,3]

print(dd['u'])

#Below it will return 0 instead of error
print(dd['xyz'])

myDic = {1:"afn"}
print(myDic[1])

#Below line throws error as it's not set to defaultDict
#print(myDic[2])


#Default Dictionary if set as list, you can use list methods on the key
dd2 = defaultdict(list)
dd2[1] = [1] #this should be list only
dd2[1].append(4)
print(dd2[1])

