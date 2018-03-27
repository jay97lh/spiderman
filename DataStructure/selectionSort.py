from sortTestHelper import sort_test_helper
import time

def selectionSort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]> arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

def main():
    length = int(input("Please input length of the arr you want to sort:"))
    arr = sort_test_helper(length)
    selectionSort(arr)

if __name__ == "__main__":
    main()
