class Sort_Algorithms(object):
    def __init__(self):
        self.sort_me = [9, 2, 1, 4, 7, 6, 5, 3, 8]

    def __str__(self):
        return str("\t[ Object Oriented Sorting Algorithms ]\n"
            f"Bubble Sort:    {self.bubble_sort(self.sort_me)}\tBig-O: O(n^2)\n"
            f"Selection Sort: {self.selection_sort(self.sort_me)}\tBig-O: O(n^2)\n"
            f"Insertion Sort: {self.insertion_sort(self.sort_me)}\tBig-O: O(n^2)\n"
            f"Heap Sort:      {self.heap_sort(self.sort_me)}\tBig-O: O(nlog(n))\n"
            f"Merge Sort:     {self.merge_sort(self.sort_me)}\tBig-O: O(nlog(n))\n"
            f"Quick Sort:     {self.quick_sort(self.sort_me)}\tBig-O: O(n)")

    def bubble_sort(self, nums):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
        return nums

    def selection_sort(self, nums):
        for i in range(len(nums)):
            lowest_value_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[lowest_value_index]:
                    lowest_value_index = j
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
        return nums

    def insertion_sort(self, nums):
        for i in range(1, len(nums)):
            item_to_insert = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > item_to_insert:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = item_to_insert
        return nums
    
    def heap_sort(self, nums):
        def heapify(nums, heap_size, root_index):
            largest = root_index
            left_child = (2 * root_index) + 1
            right_child = (2 * root_index) + 2

            if left_child < heap_size and nums[left_child] > nums[largest]:
                largest = left_child

            if right_child < heap_size and nums[right_child] > nums[largest]:
                largest = right_child

            if largest != root_index:
                nums[root_index], nums[largest] = nums[largest], nums[root_index]
                heapify(nums, heap_size, largest)

        def heap_sorter(nums):
            n = len(nums)

            for i in range(n, -1, -1):
                heapify(nums, n, i)

            for i in range(n - 1, 0, -1):
                nums[i], nums[0] = nums[0], nums[i]
                heapify(nums, i, 0)
        heap_sorter(nums)
        return nums

    def merge_sort(self, nums):
        def merge(left_list, right_list):
            sorted_list = []
            left_list_index = right_list_index = 0
            left_list_length, right_list_length = len(left_list), len(right_list)

            for _ in range(left_list_length + right_list_length):
                if left_list_index < left_list_length and right_list_index < right_list_length:
                    if left_list[left_list_index] <= right_list[right_list_index]:
                        sorted_list.append(left_list[left_list_index])
                        left_list_index += 1
                    else:
                        sorted_list.append(right_list[right_list_index])
                        right_list_index += 1
                elif left_list_index == left_list_length:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1
                elif right_list_index == right_list_length:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1
            return sorted_list

        def merge_sorter(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left_list = merge_sorter(nums[:mid])
            right_list = merge_sorter(nums[mid:])
            return merge(left_list, right_list)
        merge_sorter(nums)
        return nums
    
    def quick_sort(self, nums):
        def partition(nums, low, high):
            pivot = nums[(low + high) // 2]
            i = low - 1
            j = high + 1
            while True:
                i += 1
                while nums[i] < pivot:
                    i += 1
                j -= 1
                while nums[j] > pivot:
                    j -= 1
                if i >= j:
                    return j
                nums[i], nums[j] = nums[j], nums[i]

        def quick_sorter(nums):
            def _quick_sorter(items, low, high):
                if low < high:
                    split_index = partition(items, low, high)
                    _quick_sorter(items, low, split_index)
                    _quick_sorter(items, split_index + 1, high)

            _quick_sorter(nums, 0, len(nums) - 1)
        quick_sorter(nums)
        return nums

if __name__ == "__main__":
    print(Sort_Algorithms())
    
    
