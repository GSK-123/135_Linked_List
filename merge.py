class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    dummy = ListNode(0)
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l1 else l2
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

def return_list(head):
    current = head
    while current:
        print(current.val, end=' -> ')
        current = current.next
    print('None')

l1 = linked_list([1, 3, 5])
l2 = linked_list([2, 4, 6])
merged_list = merge(l1, l2)
return_list(merged_list)
