def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        # 选择基准值
        pivot = arr[0]
        # 小于基准值的数组
        less = [i for i in arr[1:] if i <= pivot]
        # 大于基准值的数组
        greater = [i for i in arr[1:] if i > pivot]
        # 拼接小的和大的组成完整的排序后的数组
        return quickSort(less) + [pivot] + quickSort(greater)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(quickSort([5, 3, 6, 2, 10]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
