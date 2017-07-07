def sort(arr):
	length = len(arr)
	if length == 1:
		return arr
	else:
		new_arr = []
		left_arr = sort(arr[:length//2])
		right_arr = sort(arr[length//2:])
		i = 0
		j = 0
		left_length = len(left_arr)
		right_length = len(right_arr)
		while i < left_length or j < right_length:
			if i >= left_length:
				new_arr.append(right_arr[j])
				j += 1
			elif j >= right_length:
				new_arr.append(left_arr[i])
				i +=1
			else:
				if left_arr[i] < right_arr[j]:
					new_arr.append(left_arr[i])
					i += 1
				else:
					new_arr.append(right_arr[j])
					j += 1
		return new_arr
