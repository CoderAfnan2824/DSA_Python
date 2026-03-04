
array = [1,5,6,7,4]

#1. enumerate(iterable, start=1)
#if start is 2, first index starts from 2 instead of 0

#It returns (index, value) pair

for i in range(len(array)):
    print(array[i])

print('------------------')
#above code can be written using enumerate as below
for i, value in enumerate(array):
    print(value)

new_array = list(enumerate(array))
#Only enumerate returns an object

#2. Reversed
print(reversed(array)) #returns an object
print(list(reversed(array))) #returns a list

#3 range
print(list(range(10))) #returns an object
print(list(range(5,10)))
print(list(range(5,15,3)))

print(list(zip([1,2,3],[4,5],[6])))