class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1 and not l2:
        return None
    elif not l1 :
        curr = l2
        res = l2
        l2_curr = l2.next
        l1_curr = l1
    elif not l2 or l1.val < l2.val:
        curr = l1
        res = l1
        l1_curr = l1.next
        l2_curr = l2
    else:
        curr = l2
        res = l2
        l2_curr = l2.next
        l1_curr = l1
    
    while l2_curr or l1_curr:
        if not l2_curr:
            curr.next = l1_curr
            curr = curr.next
            l1_curr = l1_curr.next
        elif not l1_curr:
            curr.next = l2_curr
            curr = curr.next
            l2_curr = l2_curr.next
        else:
            if l1_curr.val < l2_curr.val:
                curr.next = l1_curr
                curr = curr.next
                l1_curr = l1_curr.next
            else:
                curr.next = l2_curr
                curr = curr.next
                l2_curr = l2_curr.next
    return res

def mergeTwoListsRecursive(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoListsRecursive(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoListsRecursive(l1, l2.next)
        return l2

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

mergeTwoListsRecursive(l1, l2)