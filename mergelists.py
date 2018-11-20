"""
This problem has asked that SORTED lists be merged and the entries should be sorted. 
This uses a heap to fasten the process of forming a sorted array as finding the 
smallest element in a heap is fast. We heapify the the combined list of lists and 
then pull the smallest among the first elements of all lists and then push it into 
the merged list while making the next element in the heap available for comparison
in the next iteration.

"""
import heapq

def merge_lists(list_here):
    merged=[]

    heap = [(entry[0], i, 0) for i, entry in enumerate(list_here) if entry]
    heapq.heapify(heap)

    while heap:
        value, list_index, element_index= heapq.heappop(heap)
        merged.append(value)

        if (element_index + 1 < len(list_here[list_index])):
            next_entry= ( list_here[list_index][element_index+1],
                            list_index, 
                            element_index+1)
            heapq.heappush(heap, next_entry)

    return merged                



lists_to_be_merged=[[8, 15, 30], [100, 200, 2000], [100, 260, 300]]

print(merge_lists(lists_to_be_merged))