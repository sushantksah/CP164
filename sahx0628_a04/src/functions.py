"""
-------------------------------------------------------
[Functions File]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from Queue_circular import Queue
from Priority_Queue_array import Priority_Queue
from copy import deepcopy


# Task 3
def queue_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source queue into separate target queues with values
    alternating into the targets. At finish source queue is empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target1, target2 = queue_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - a queue (Queue)
    Returns:
        target1 - contains alternating values from source (Queue)
        target2 - contains other alternating values from source (Queue)
    -------------------------------------------------------
    """
    target1 = Queue()
    target2 = Queue()

    while not source.is_empty():
        target1.insert(source.remove())

        if not source.is_empty():
            target2.insert(source.remove())

    return deepcopy(target1), deepcopy(target2)

# Task 5


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """

    target1 = Priority_Queue()
    target2 = Priority_Queue()
    if not source.is_empty():
        while not source.is_empty():
            temp = source.remove()
            if temp < key:
                target1.insert(temp)
            else:
                target2.insert(temp)

    return target1, target2
