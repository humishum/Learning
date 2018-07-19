import numpy as np
#referenced from https://engineering.ucsb.edu/~shell/che210d/numpy.pdf
# ------------------Arrays--------------------
    # similar to list, every element is same type
arr =  np.array([1, 4, 5, 8], float)
print('This is a np array: ')
print (arr)
print(type(arr)) # type and class are essentially the same in python

#array elements are treated just like list elements
arr[:2] # returns first two elements
arr[3]#returns element of 3rd index aka 8
arr[0]= 5. # changed first element to 5
print(arr)

arr2 = np.array([[1,2,3],[4,5,6]],float)
print(arr2[1,:])#prints everything in row(index 1) 1 {4,5,6}
print(arr2[:,2])#prints everything in column (index2) 2 {3,6}
print(arr2[-1:,-2:])#prints {5,6}
print(arr2.shape)#returns tuple with the size of array {(2,3)}
print(arr2.dtype)# tells you what type of values are stored by the Arrays
len(arr2) # returns the length of the first axis
2 in arr2 # returns true
0 in arr2 #returns false

arr3 = np.array(range(10), float) # arr3  = {1,2,...8,9}
arr3 = arr3.reshape((5,2)) # arr3 = [[0,1],[2,3] ,,,[8,9]]

arr2.tolist()# makes arr2 back into a list from a numpy array

s = arr.tostring()#converts arr to string, unreadable to humans, used to save space
np.fromstring(s)#converts back into np array

arr.fill(0)#fills array with values of 0

arr2.transpose()# transposes array, AKA final two axes switched
arr2.flatten()#flattens a multidimensional array into 1D
#np.concatenate((arr,arr2,arr3))#concatenates arrays
#can also concatenate along a specific axis of two arrays
# np.concatenate((a,b), axis =0)

arr[:,np.newaxis]# can increase dimensionality of an array
np.arange(5,dtype=float) #is similar to range func but returns an array
np.ones((2,3), dtype=float)# fills with ones, np.zeros(7,dtype=int), fills with zeros
#np.zeros_like(a) #creates array with same dimensions as 'a', also works for ones_like
np.identity(4,dtype=float) # creates identity matrix of row and column size 4
np.eye(4, k =1 , dtype=float )# returns array with 1s along kth diagonal

# array operations +,-,*,/,%,** are done elementwise, arrays should be same size.
#even for 2D arrays, multiplication is elementwise
#if arrays arent the same size then the smaller one is broadcasted across the larger
a = np.array([[1, 2], [3, 4], [5, 6]], float)
b = np.array([-1, 3], float)
print(a+b)
np.floor(a)#lower int
np.ceil(a)#upper int
np.rint(a)#nearest rounded int
np.pi
np.e

for x in b: # array iteration
    print(x)

for x in a:# iteration over 2D Array goes first axis, then next next next
    print(x)

for (x,y) in a:#multiple assignment
    print x*y

b.sum() # returns sum of all elements
np.sum(b)
b.prod() # returns product of all elements
np.prod(b)
b.mean()# avg of all elements
b.var()#variance
b.std()#std dev
a.min()# min element value
a.max()#max element value
a.argmin()#returns INDEX of min value
a.argmax()#returns INDEX of max value
#for 2D arrays, each of the above can take additional (axis=x) argument to choose form an axis
# for ex: a.mean(axis=0)

sorted(a)#sorts array, simple
a.sort(a)

a.clip(0,5)# can clip all values to be within those two values
np.unique(a)# unique elements can be extracted from array
a.diagonal()#returns diagonal if 2D array

# a > b returns a boolean array that compares a and b values elementwise
# any(c) returns if there are any true elements in Boolean array
#all(c) returns if there ALL elements are true in boolean array

#np.logical_and(a>0,a<3) returns boolean array with constraints
#np.where idk what this does but where(boolarray,truearray,falsearray)
a.nonzero()# gives tuple of indices of the nonzero values in array
np.isnan(a)
# array selectors to filter subests of elements of other array a for value in variable
a = np.array([[6, 4], [5, 9]], float)
a[a>=6]# returns array [6,9]
a[np.logical_and(a > 5, a < 9)]#returns 6
a = np.array([2, 4, 6, 8], float)
b = np.array([0, 0, 1, 3, 2, 1], int)
#a[b] ->array([ 2., 2., 4., 8., 6., 4.])
np.dot(a,b)#gives dot product of two arrays, also generalized to matrix multiplication

np.random.seed(293423)
np.random.rand(5)
np.nandom.rand(2,3)
