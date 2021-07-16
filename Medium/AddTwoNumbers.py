# https://leetcode.com/problems/add-two-numbers/

import sys
sys.path.append("../")

from Helpers.List import ListNode, addNode, arrToList, showList

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    finalList = None

    lc1 = l1
    lc2 = l2
    current = None
    carryOver = 0
    singleDigit = 0

    while lc1 is not None or lc2 is not None:
        availableList = list(filter(None, [lc1, lc2]))
        
        if len(availableList) != 2:
            if lc1 is None:
                current = lc2
            else:
                current = lc1

            total = current.val + carryOver

            singleDigit = total % 10
            carryOver = total // 10

            if current.next is None:
                finalList = addNode(finalList, singleDigit)

                if carryOver > 0:
                    finalList = addNode(finalList, carryOver)
            else:
                finalList = addNode(finalList, singleDigit)
            
            if lc1 is None:
                lc2 = lc2.next
            else:
                lc1 = lc1.next

        else:
            total = lc1.val + lc2.val + carryOver

            singleDigit = total % 10
            carryOver = total // 10

            finalList = addNode(finalList, singleDigit)

            if lc1.next is None and lc2.next is None and carryOver > 0:
                finalList = addNode(finalList, carryOver)

            lc1 = lc1.next
            lc2 = lc2.next

    
    print(carryOver)
    
    return finalList


if __name__ == '__main__':
    arr1 = [5]
    arr2 = [5]

    l1 = arrToList(arr1)
    l2 = arrToList(arr2)

    print("hello")

    showList(addTwoNumbers(l1, l2))
