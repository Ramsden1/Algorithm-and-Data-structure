def insertion_sort_a(array):
	# asending 
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i>=0 and array[i]>key:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = key
	return array

def insertion_sort_d(array):
	#desending
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] < key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

    return array

a = insertion_sort_a([6,2,1,6,9,5,4,5,3])
b = insertion_sort_d([6,2,1,6,9,5,4,5,3])
print(a,b)
