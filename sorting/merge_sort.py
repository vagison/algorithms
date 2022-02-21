# Merge sort algorithm
# In computer science, merge sort (also commonly spelled as mergesort) is an efficient, general-purpose, and comparison-based sorting algorithm.
# Most implementations produce a stable sort, which means that the order of equal elements is the same in the input and output.
# Merge sort is a divide and conquer algorithm that was invented by John von Neumann in 1945.
# A detailed description and analysis of bottom-up merge sort appeared in a report by Goldstine and von Neumann as early as 1948.

# Testing cases
# test = []
# test = [4, 1, 3, 9, 7]
# test = [55, 1]
# test = [12, 15, 23, 4, 6, 10, 35, 28]
# test = [4, 6, 10, 12, 15, 23, 28, 35]
# test = [12, 15, 23, 4, 6, 10, 35]
# test = [35, 28, 23, 15, 12, 10, 6, 4]
# test = [12]
# test = [12, 4]
# test = [12, 15, 23, 4, 6, 10, 35, 28, 100, 130, 500, 1000, 235, 554, 75, 345, 800, 222, 333, 888, 444, 111, 666, 777, 60]
# test = [12, 15, -23, -4, 6, 10, -35, 28]
# test = [12, 12, 23, 4, 6, 6, 10, -35, 28]
# test = [12, 12, 12, 12, 12]

# Defining merging function (takes two sorted arrays)
def merge(left, right):
    leftLength = len(left)
    rightLength = len(right)

    total = []
    totalLength = len(left) + len(right)

    index = 0
    indexLeft = 0
    indexRight = 0

    while index < totalLength:
        while indexLeft < leftLength and indexRight < rightLength:
            if left[indexLeft] <= right[indexRight]:
                total.append(left[indexLeft])
                indexLeft += 1

            else:
                total.append((right[indexRight]))
                indexRight += 1

            index += 1

        while indexLeft < leftLength:
            total.append(left[indexLeft])
            indexLeft += 1
            index += 1

        while indexRight < rightLength:
            total.append(right[indexRight])
            indexRight += 1
            index += 1

    return total

# Defining merge sort function, which recursively calls itself till the resulting array length is one, then merging back


def mergeSort(arr):
    arrLength = len(arr)

    if arrLength <= 1:
        return arr

    else:
        midpoint = arrLength // 2

        leftSide = mergeSort(arr[0:midpoint])
        rightSide = mergeSort(arr[midpoint:arrLength])

        return merge(leftSide, rightSide)
