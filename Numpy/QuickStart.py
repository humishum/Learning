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
