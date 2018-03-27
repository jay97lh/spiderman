from sortTestHelper import sort_test_helper

def insertion_sort(list):
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j-1]:
                list[j-1], list[j] = list[j], list[j-1]

def main():
    list = sort_test_helper(10)
    print(list)
    insertion_sort(list)
    print(list)


if __name__ == '__main__':
    main()