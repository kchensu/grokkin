from Node import Node


def startOfLinkedListCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    while head != slow:
        slow = slow.next
        head = head.next
    return head.value


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

head.next.next.next.next.next.next = head.next.next
print(startOfLinkedListCycle(head))

head.next.next.next.next.next.next = head.next.next.next
print(startOfLinkedListCycle(head))

head.next.next.next.next.next.next = head
print(startOfLinkedListCycle(head))
