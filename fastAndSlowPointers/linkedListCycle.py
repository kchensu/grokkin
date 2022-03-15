from Node import Node


def linkedListCycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def linkedListCycleLength(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            current = slow
            lenght = 0
            while True:
                current = current.next
                lenght += 1
                if current == slow:
                    break
            return lenght


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
# No cycle test
print(f'Contains a cycle? {linkedListCycle(head)}')

# contains a cycle test
head.next.next.next.next.next.next = head.next.next
print(f'Contains a cycle? {linkedListCycle(head)}')
print(f'Cycle length {linkedListCycleLength(head)}')
