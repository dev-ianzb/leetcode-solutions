# 876. Middle of the Linked List

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.


# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.


# Example 2:

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Constraints:
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100


# My first attempt (didn't return a linked list):
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def middleNode(self, head):
        # toList = []
        # outList = []
        # curr = head
        # while curr:
        #     toList.append(curr.val)
        #     curr = curr.next
        # length = len(toList)
        # if length % 2 == 0:
        #     start = length /2
        #     for i in range(start, len(toList)):
        #         outList.append(toList[i])
        # else:
        #     start = (length - 1)/2
        #     for i in range(start, len(toList)):
        #         outList.append(toList[i])
        # return outList

#My final unrefined solution:
class Solution(object):
    def middleNode(self, head):
        Tonode = []   
        curr = head
        while curr:
            Tonode.append(curr)
            curr = curr.next
        length = len(Tonode)
        if length % 2 == 0:
            start = length / 2
        else:
            start = (length - 1) / 2
        return Tonode[start]