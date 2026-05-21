def BinarySearch(arr, i, j, x):
    # assumes that arr is sorted
    if j < i: return None
    m = (i + j) // 2

    if arr[m] == x: return m
    elif arr[m] < x: return BinarySearch(arr, m+1, j, x)
    else: return BinarySearch(arr, i, m-1, x)

def InsertionSort(arr, n=None):
    if n is None: n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1

def Merge(A, i, m, j):
    """
    Helper function for Merge-sort. For internal use.

    
    """

    nL = m - i + 1
    nR = j - m
    L, R = A[i:m+1], A[m+1:j+1]
    p, q, k = 0, 0, i

    while p < nL and q < nR:
        if L[p] < R[q]:
            A[k] = L[p]
            p += 1
        else: 
            A[k] = R[q]
            q += 1
        k += 1
    
    while p < nL:
        A[k] = L[p]
        p += 1
        k += 1
    while q < nR:
        A[k] = R[q]
        q += 1
        k += 1

def MergeSort(arr, i=None, j=None):
    if i is None: i = 0
    if j is None: j = len(arr)-1
    if i < j:
        m = (i + j) // 2
        MergeSort(arr, i, m)
        MergeSort(arr, m+1, j)
        Merge(arr, i, m, j)

if __name__ == "__main__":
    A = [3, 13, 4, 2, 7, 3, 6, 0, 1, 6, 8, 32, 8, -4]
    MergeSort(A)

    print(f"A sorted: {A=}")

    i = BinarySearch(A, 0, len(A), 4)
    j = BinarySearch(A, 0, len(A), 3)

    print(i)
    print(j)
