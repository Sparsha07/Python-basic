
def _sum(arr):

	sum=0
	
	# iterate through the array
	# and add each element to the sum variable
	# one at a time
	for i in arr:
		sum = sum + i
		
	return(sum)


arr=[]
# input values to list
arr = [12, 3, 4, 15]

# calculating length of array
n = len(arr)

ans = _sum(arr)

# display sum
print ('Sum of the array is ', ans)


