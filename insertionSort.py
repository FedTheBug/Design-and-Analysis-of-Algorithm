#Creating insertionsort function
def insertionSort(arr):
	for i in range (1,len(arr)):
		key = arr[i]
		j = i-1
		while j>=0 and arr[j]>key:
			arr[j+1] = arr[j]
			j = j-1
		arr[j+1] = key

arr = [12,2,5,4,6]
insertionSort(arr)
for i in range (len(arr)):
	print (arr[i], end= ' ')