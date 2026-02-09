import sys

sys.stdin =  open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

array = [1,5,6,7,4]

# 1. len function
print(len('Afnan'))

# 2. sorted function
print(sorted(array)) #prints sorted array, but doesn'y update array
print(sorted(array, reverse=True)) #print decending sorted array

# 3. sort function
array.sort() #sorts array and update
print(array)
array.sort(reverse=True) #sorts array in decending order and update
print(array)

# 4. Sort absolute values
arr1 = [1, -5, 6, -7, 4]
arr1.sort(key = lambda x: abs(x))
print(arr1)

# 5. Sort based on length of string
fruit_list = ['mango','apple', 'banana', 'kiwi', 'grapefruit']
fruit_list.sort(reverse=True, key = lambda x: len(x))
print(fruit_list)


def mylen(strs):
    count = 0
    for i in strs:
        count += 1
    return count

