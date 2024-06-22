class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove(head, n):
    dummy = ListNode(0)
    dummy.next = head
    x = dummy
    y = dummy
    for _ in range(n + 1):
        x = x.next
    while x:
        x = x.next
        y = y.next
    y.next = y.next.next
    return dummy.next

def linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_list(head):
    current = head
    while current:
        print(current.val, end=' -> ')
        current = current.next
    print('None')

head = linked_list([1, 2, 3, 4, 5])
n = 2
new_head = remove(head, n)
print_list(new_head)
