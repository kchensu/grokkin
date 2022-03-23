from Node import Node


def palindroneLinkedList(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    headSecondHalf = reverse(slow)
    copyHeadSecondHalf = headSecondHalf

    while head and headSecondHalf:
        if head.value != headSecondHalf.value:
            break
        head = head.next
        headSecondHalf = headSecondHalf.next
    reverse(copyHeadSecondHalf)
    if head is None or headSecondHalf is None:
        return True
    return False


def reverse(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(4)
head.next.next.next.next = Node(2)
print(palindroneLinkedList(head))
