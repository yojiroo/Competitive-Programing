class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_sum = 0
        l2_sum = 0
        for i in range(len(l1)):
            l1_sum += l1_sum*10 + l1[i]
            l2_sum += l2_sum*10 + l2[i]
        
        l = l1_sum + l2_sum
        l = str(l)
        l = list(l)
        return l