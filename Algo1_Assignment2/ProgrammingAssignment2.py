import os

def quick_sort (arr):
    def swap(l, a,b):
        temp = l[a]
        l[a] = l[b]
        l[b] = temp
        return l
    def find_median(x):
        candi = sorted([x[0],x[-1],x[int(ceil(len(x)/2.))-1]])[1]
        return swap(x, 0, x.index(candi))

    if len(arr)==0 or len(arr)==1:
        return arr
    arr = find_median(arr)
    pivot = arr[0]
    i = 1
    for j in range(i,len(arr)):
        if arr[j]<pivot:
            arr = swap(arr, i, j)
            i += 1
    i -= 1
    arr = swap(arr, 0, i)
    return quick_sort(arr[:i])+[arr[i]]+quick_sort(arr[i+1:])

from math import ceil
def quick_sort_count (arr, index, median=False):
    def swap(l, a,b):
        temp = l[a]
        l[a] = l[b]
        l[b] = temp
        return l
    def find_median(x):
        candi = sorted([x[0],x[-1],x[int(ceil(len(x)/2.))-1]])[1]
        return swap(x, 0, x.index(candi))

    if len(arr)==0 or len(arr)==1:
        return arr, 0
    if index != 0:
        arr = swap(arr, index, 0)
    if median:
        arr = find_median(arr)
    pivot = arr[0]
    i = 1
    for j in range(i,len(arr)):
        if arr[j]<pivot:
            arr = swap(arr, i, j)
            i += 1
    arr = swap(arr, 0, i-1)
    arr[:i-1], t1 = quick_sort_count(arr[:i-1], index, median)
    arr[i:], t2 = quick_sort_count(arr[i:], index, median)
    return arr, len(arr)+t1+t2-1

def test (l):
    from random import shuffle
    x=range(l)
    shuffle(x)
    print "The original data set is ", x
    print "The sorted array is ", quick_sort(x)

if __name__ == "__main__":
    test(20)


def run_quicksort (arr, index, median):
    _,result = quick_sort_count(arr, index, median)
    print result


def main ():
    arr = []
    sent_file = open("Algo1QuickSort.txt")
    with sent_file as datafile:
        for row in datafile:
            arr.append(int(row))
    arr2 = list(arr)
    arr3 = list(arr)
    _,result = quick_sort_count(arr, 0)
    print "Assign the 1st element as pivot:", result
    _,result = quick_sort_count(arr2, -1)
    print "Assign the last element as pivot:", result
    _,result = quick_sort_count(arr3, 0, True)
    print "Assign the 'median' element as pivot:", result

if __name__=="__main__":
    main()
