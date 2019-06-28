def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    TreeList = [head]
    
    while head is not None:
        head = head.next
        
        if (head in TreeList):
            return True
        else:
            TreeList.append(head)
    
    return False
        
        