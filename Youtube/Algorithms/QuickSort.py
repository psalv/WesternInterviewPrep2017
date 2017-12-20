

def partition(ar, start, end):
    """
    Partition: select a pivot, and all elements to the left are lesser and all elements to the right are greater
    Once we partition can break into two subproblems (sorting the left and the right subarrays)

    Return index of the partition index
    """

    # Arbitrarily choose the last index as the pivot
    pivot = ar[end]

    partitionIndex = start

    for i in range(start, end):
        if ar[i] <= pivot:

            # Swap the partition index and the lower value
            temp = ar[i]
            ar[i] = ar[partitionIndex]
            ar[partitionIndex] = temp

            partitionIndex += 1

    # At the end we need to swap the pivot (which is at the end) with the partitionIndex
    temp = ar[end]
    ar[end] = ar[partitionIndex]
    ar[partitionIndex] = temp

    return partitionIndex


def quicksort(ar, start, end):
    """
    O(nlgn) average case
    O(n^2) worst case

    An inplace sorting algorithm, so takes constant space

    We almost always avoid the worst case so it ends up being a fairly good sorting algorithm

    The most practical choice for a sorting algorithm


    The best case is when we have balanced sorting, when each of the subarrays have sizes close to n/2, where n is num elements to be sorted
    """

    # If the start and end have met then we are at our base case so we finish (it is an array of len <= 1, implicitly sorted)
    if start < end:

        # Partition will pick a pivot, and then put everything to the left of it be less than it and opposite to the right
        partitionIndex = partition(ar, start, end)

        # We know recurse on the left subarray
        quicksort(ar, start, partitionIndex - 1)

        # And on the right subarray
        quicksort(ar, partitionIndex + 1, end)


def test():
    x = [23, 1, 2, 1, -123, 123, 343, 4586873, 234]
    quicksort(x, 0, len(x) - 1)
    print(x)


test()

