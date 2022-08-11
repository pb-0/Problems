# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        self.helper(head)

    def helper(self, root):
        if root == None:
            return
        print(root.getNext())
        self.helper(root.getNext())
        root.printValue()