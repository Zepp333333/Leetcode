from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class LinkedList:
#     def __init__(self, node: ListNode = None) -> None:
#         self.start_node = node


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        start_node = ListNode()

        def sum_list(l1, l2, node, remainder):
            temp_sum = l1.val + l2.val + remainder
            node.val = temp_sum % 10
            remainder = temp_sum // 10
            if (not l1.next) and (not l2.next):
                print(f"not both")
                if remainder == 0:
                    return
                else:
                    node.next = ListNode()
                    node.next.val = remainder
                    return
            elif not l1.next:
                print(f"not l1")
                node.next = ListNode()
                sum_list(ListNode(0), l2.next, node.next, remainder)
            elif not l2.next:
                print(f"not l2")
                node.next = ListNode()
                sum_list(l1.next, ListNode(0), node.next, remainder)
            else:
                node.next = ListNode()
                sum_list(l1.next, l2.next, node.next, remainder)

        sum_list(l1, l2, start_node, 0)
        return start_node


def make_list(lst: List[int]):
    start_node = ListNode()
    n = start_node
    n.val = lst[0]
    for i in lst[1:]:
        n.next = ListNode()
        n = n.next
        n.val = i
    return start_node


def print_list(node: ListNode):
    print(node.val)
    if not node.next:
        return
    else:
        print_list(node.next)


s = Solution()
# r = s.addTwoNumbers(
#     ListNode(2, ListNode(4, ListNode(3, None))),
#     ListNode(5, ListNode(6, ListNode(4, None))),
# )

# r2 = s.addTwoNumbers(ListNode(0), ListNode(0))
r3 = s.addTwoNumbers(make_list([2, 4, 9]), make_list([5, 6, 4, 9]))
# r3 = s.addTwoNumbers(make_list([5, 6, 4, 9]), make_list([2, 4, 9]))
# r3 = s.addTwoNumbers(make_list([3]), make_list([2, 4]))
print_list(r3)
# print_list(r)
# print_list(r2)
# print_list(r3)
