class Sort:
    def selection_sort(self, a):
        # 首先，找到数组中最小的那个元素，其次，将它和数组的第一个元素交换位置。
        # 再次，在剩下的元素中找到最小的元素，将它和数组的第二个元素交换位置。
        # 如此往复，直到将整个数组排序。
        N = len(a)
        for i in range(N):
            min = i
            for j in range(i+1, N):
                if a[j] < a[min]:
                    min = j
            tmp = a[i]
            a[i] = a[min]
            a[min] = tmp
        return a

    def insertion_sort(self, a):
        # 通常人们整理桥牌的方法是一张一张的来，将每一张牌插入到其他已经有序的牌中的适当位置。
        # 为了给插入的元素腾出空间，需要将其余所有元素在插入之前都向右移动一位。
        N = len(a)
        for i in range(1, N):
            j = i
            while j > 0:
                if a[j] < a[j-1]:
                    tmp = a[j-1]
                    a[j-1] = a[j]
                    a[j] = tmp
                j -= 1
        return a

    # 快速排序是一种分治的排序算法，它将一个数组分成两个子数组，将两部分独立地排序。
    def quick_sort(self, a, low, high):

        # 将每个元素与pivot进行比较，并将小于pivot的所有元素移动到pivot的左侧，将大于pivot的所有元素移动到pivot右侧。
        def Partition(a, low, high):
            pivot = a[low]
            while low < high:
                while low < high and a[high] >= pivot:
                    high -= 1
                a[low] = a[high]
                while low < high and a[low] <= pivot:
                    low += 1
                a[high] = a[low]
            a[low] = pivot
            return low

        if low < high:
            pivot = Partition(a, low, high)
            self.quick_sort(a, low, pivot-1)
            self.quick_sort(a, pivot+1, high)
        return a


if __name__ == '__main__':
    L = [5, 9, 1, 11, 6, 7, 2, 4]
    sort = Sort()
    sort_list = sort.quick_sort(L, 0, len(L)-1)
    print(sort_list)