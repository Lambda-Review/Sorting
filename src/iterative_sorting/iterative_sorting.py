# TO-DO: Complete the selection_sort() function below 
# * Big O = 0(n2)
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        print(f"cur_index = {i}")
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            print(f"if arr[j] ({arr[j]}) < arr[smallest_index] ({arr[smallest_index]}) ")
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                # print(f"arr[{j}] = {arr[smallest_index]}")
                print(f"smallest_index = {arr[j]}")
        # TO-DO: swap
        print(arr)
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        print(arr)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr




# Selection sort test
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# arr2 = []
# arr3 = [0, 1, 2, 3, 4, 5]

selection_sort(arr1) # *  =>  [0,1,2,3,4,5,6,7,8,9]
# selection_sort(arr2) # *  => []
# selection_sort(arr3) # *  => [0,1,2,3,4,5]

# * Bubble sort tests
# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# arr2 = []
# arr3 = [0, 1, 2, 3, 4, 5]


# bubble_sort(arr1), [0,1,2,3,4,5,6,7,8,9]
# bubble_sort(arr2), []
# bubble_sort(arr3), [0,1,2,3,4,5]

# * Counting sort tests