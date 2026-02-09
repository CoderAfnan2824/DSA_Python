
array = [1,5,6,7,4]

#1. enumerate

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