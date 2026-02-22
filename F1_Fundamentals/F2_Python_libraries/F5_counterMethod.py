from collections import Counter
#Counters are used to find the frquency in the list
#Useful in hashing
array = [1,2,4,1,2,3,2,5,1]

arr = Counter([1,2,4,1,2,3,2,5,1])
print(arr[1])
#Counter stores value as index and count of that index as value
# arr : 1 -> 3, 2 -> 2, 3 -> 1, 4 -> 1, 5 -> 1

#return top 2 most commonly occuring element
print(arr.most_common(2))
print(arr.most_common(3)) 
#if count same, first inserted will come first

# 1 -> appear 3 times
# 2 -< appear 3 times
# 4,3,5 -> appear 1 time
#elements create array with element appearing for it's count times
new_list = list(arr.elements())
print(new_list)
# [ 1,1,1,2,2,2,4,3,5]

arr.update([7,3]) #add 7,3 to counter 
print(list(arr.elements()))

c1 = Counter([4,4,1,5,2,2,6])
c2 = Counter([1,5,2,2,3])

c3 = c1-c2
c4 = c2+c1

print(list(c3.elements()))
#[4,6]
print(list(c4.elements()))
#[1,5,5,3,4,6]

c5 = c1 & c2
#It's like intersection
print(list(c5.elements()))

c6 = c1 | c2
#It's like getting max for each element
print(list(c6.elements()))
