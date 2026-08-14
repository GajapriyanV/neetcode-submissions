# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        dummy = ListNode()

        for head in lists:
            if head:
                heap.append((head.val, 0, head))
        
        cur = dummy
        while heap:
            cur_val, idx, cur_node = heapq.heappop(heap)
            cur.next = cur_node
            cur = cur.next

            if cur_node.next:
                nxt_node = cur_node.next
                heapq.heappush(heap, (nxt_node.val, idx + 1, nxt_node))
        
        return dummy.next


        

        