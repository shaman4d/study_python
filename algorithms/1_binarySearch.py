def binary_search(L, item):
	low = 0
	high = len(L)
	counter = 0
	while low <= high:
		counter+=1
		print(f"try {counter}")
		mid = (low+high)//2
		guess = L[mid]
		if guess == item:
			return mid
		if item < guess:
			high = mid - 1
		else:
			low = mid + 1
	return None

L = [1,2,3,4,5,7,13,19]
print(binary_search(L, 1))