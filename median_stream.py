"""Given a stream of unsorted integers, find the median element in sorted order at any given time."""

#I will use two heaps to have access of the median in O(1) time. 

"""
This forms a min heap and other is max heap. I take the first element in min heap and then compare
the next element to this element into min or max heap. If the heaps are imbalanced by more than one 
element. We rebalance the heaps by shifting elements.
"""

