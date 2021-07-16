from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def listLength(node: ListNode, val: int = 0):
    if node is None:
        return val

    return 1 + val + listLength(node.next)


def addNode(node: ListNode, val: int):
    if node is None:
        return ListNode(val=val)

    current = node

    while current.next is not None:
        current = current.next

    current.next = ListNode(val=val)

    return node


def showList(node: ListNode):
    if node is None:
        print()
        return

    print(node.val, end=" ")
    showList(node.next)


def arrToList(nums: List[int]) -> ListNode:
    node: ListNode = None

    for x in nums:
        node = addNode(node, x)

    return node


# if __name__ == '__main__':
#     print("Hello")

#     ll = arrToList([1, 3, 5, 4])

#     showList(ll)
#     print(listLength(ll))
