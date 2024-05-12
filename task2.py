import heapq

def merge_k_lists(lists):
    heap = []
    for i, lst in enumerate(lists):
        for j in lst:
            heapq.heappush(heap, j)
    
    merged_list = []

    while heap:
        merged_list.append(heapq.heappop(heap))

    return merged_list

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)