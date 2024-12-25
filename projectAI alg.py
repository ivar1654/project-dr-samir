def counting_sort(arr):
    
    min_value = min(arr)
    max_value = max(arr)

   
    count = [0] * (max_value - min_value + 1)


    for num in arr:
        count[num - min_value] += 1

   
    for i in range(1, len(count)):
        count[i] += count[i - 1]


    output = [0] * len(arr)
    for num in reversed(arr):
        count[num - min_value] -= 1
        output[count[num - min_value]] = num


    for i in range(len(arr)):
        arr[i] = output[i]


arr = [22, 2, 25, 8, 43, 3, 2, 76]
print("orignal matrix :", arr)
counting_sort(arr)
print("ordered matrix :", arr)