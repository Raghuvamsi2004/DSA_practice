class node():
    def __init__(self,data):
        self.data = data #to store the data
        self.next = None #point to next node initially none


node1 = node(10)
node2 = node(20)
node3 = node(30)

node1.next = node2
node2.next = node3

current = node1
while current:
    print(current.data)
    current = current.next























class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)   # start node
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

           
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


 