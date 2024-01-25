def monotonic_array(array):
    # write code here
    flag = True
    if array[0] > array[-1]:
        for i in range(1, len(array)):
            if array[i - 1] < array[i]:
                flag = False
    else:
        for i in range(1, len(array)):
            if array[i - 1] > array[i]:
                flag = False

    return flag


print(monotonic_array([3, 2, 1]))
print(monotonic_array([1, 2, 3]))
print(monotonic_array([-3, -2, -1]))
print(monotonic_array([-1, -2, -3]))
print(monotonic_array([3,3,2,1,2]))
print(monotonic_array([1,0,2,3]))
