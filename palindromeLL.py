class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    stack = []
    
    while head is not None:
        print("head.val: " + str(head.val))
        if head.val not in stack:
            stack.append(head.val)
        else:
            if head.val is not stack[-1]:
                return False
            else:
                stack.pop()
        head = head.next
    return not stack or len(stack) == 1


head = ListNode(-129)
head.next = ListNode(-129)
isPalindrome(head)