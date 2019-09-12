class Node:
    def __init__(self, x, nextNode = None):
        self.val = x
        self.next = nextNode
 
def printList(l):
    value = []
    while(l):
        value.append(l.val)
        l = l.next
    print(value[::-1])
 
def addTwoNumbers(L_1, L_2):
    """
    :type L_1: Node
    :type L_2: Node
    :rtype: Node
    """
    sum = L_1.val + L_2.val
    carry = sum // 10
 
    L_3 = Node(sum%10)
    P_1 = L_1.next
    P_2 = L_2.next
    P_3 = L_3
    while(P_1 != None or P_2 != None):
        sum = carry + ( P_1.val if P_1 else 0) + ( P_2.val if P_2 else 0)
        carry = sum//10
        P_3.next = Node(sum % 10)
        P_3 = P_3.next
        P_1 = P_1.next if P_1 else None
        P_2 = P_2.next if P_2 else None
 
    if(carry > 0):
        P_3.next = Node(carry)
 
    return L_3

L_1 = Node(9, Node(8, Node(7)))
L_2 = Node(8, Node(7, Node(4)))
L_3 = addTwoNumbers(L_1, L_2)
printList(L_3)