import timeit

start = timeit.default_timer()

#Your statements here
# Selection sort in Python


def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data =  [11, 12, 15, 20, 26, 34, 55, 67, 71, 98]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
stop = timeit.default_timer()

print('Time: ', stop - start)