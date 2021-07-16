# https://leetcode.com/problems/merge-two-sorted-lists/

from ..Helpers.List import ListNode, addNode


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    finalList = None

    lc1 = l1
    lc2 = l2
    smallest = None

    while lc1 is not None or lc2 is not None:
        availableList = list(filter(None, [lc1, lc2]))

        if len(availableList) != 2:
            if lc1:
                smallest = lc1
                lc1 = lc1.next
            else:
                smallest = lc2
                lc2 = lc2.next

        else:

            if lc2.val <= lc1.val:
                smallest = lc2
                lc2 = lc2.next
            else:
                smallest = lc1
                lc1 = lc1.next

        finalList = addNode(finalList, smallest.val)

    return finalList
