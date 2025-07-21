class Solution:
    def sortedListToBST(self, head):
        # Helper function to find the middle node
        def find_middle(start):
            slow = start
            fast = start
            prev = None

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            if prev:
                prev.next = None  # Break the list

            return slow

        # Base case: empty list
        if not head:
            return None

        # Base case: single element
        if not head.next:
            return TreeNode(head.val)

        # Recursive step
        mid = find_middle(head)
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head if head != mid else None)
        root.right = self.sortedListToBST(mid.next)

        return root
