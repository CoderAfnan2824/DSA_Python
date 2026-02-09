
array = [1,5,6,7,4]
arr1 = [1,-7,-4,4,3,6,9,8,-2,5]
fruits = ['apple', 'banana', 'grape', 'orange']
bool_list = [True, False, True, True, False]    

#1. Min in List
print(min(array))

#2. Max in List
print(max(arr1))
print(max(arr1,key = lambda x: abs(x )))

#3. Sum of List
print(sum(array)) #23
print(sum(array, start=10)) #33

#3.1 prod of list
print(prod(array)) #840


#4. len of List
print(len(fruits))

#5.
print(any(bool_list)) #True
print(all(bool_list)) #False

#6. count of element in list
print(array.count(5)) #1


def myCount(lst, element):
    count = 0
    for i in lst:
        if i == element:
            count += 1
    return count