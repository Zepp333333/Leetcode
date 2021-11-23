from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def find_ll_lenght(ll: ListNode, counter: int = 1) -> int:
            if not ll.next:
                return counter
            else:
                return find_ll_lenght(ll.next, counter + 1)
        length = find_ll_lenght(head)
        if length == 1:
            return None
        if length == n:
            return head.next

        def find_nth_and_neighbors(prev: Optional[ListNode],
                                   nth: ListNode,
                                   n_from_start: int, counter:int) -> tuple[ListNode, ListNode, ListNode]:
            if counter == n_from_start:
                return prev, nth, nth.next
            else:
                return find_nth_and_neighbors(nth, nth.next, n_from_start, counter + 1)

        prev, nth, following = find_nth_and_neighbors(None, head, length-n, 0)
        prev.next = following
        return head


def make_list(lst: List[int]):
    start_node = ListNode()
    n = start_node
    n.val = lst[0]
    for i in lst[1:]:
        n.next = ListNode()
        n = n.next
        n.val = i
    return start_node

def print_list(head: ListNode, lst: list):
    lst.append(head.val)
    if not head.next:
        return lst
    else:
        return print_list(head.next, lst)


s = Solution()
assert print_list(s.removeNthFromEnd(make_list([1,2,3,4,5]), 2), list()) == [1,2,3,5]
assert s.removeNthFromEnd(make_list([1]), 1) is None
assert print_list(s.removeNthFromEnd(make_list([1, 2]), 1), list()) == [1]
assert print_list(s.removeNthFromEnd(make_list([1, 2, 3]), 1), list()) == [1, 2]
assert print_list(s.removeNthFromEnd(make_list([1, 2, 3]), 2), list()) == [1, 3]
assert print_list(s.removeNthFromEnd(make_list([1, 2, 3]), 3), list()) == [2, 3]
assert print_list(s.removeNthFromEnd(make_list([1, 2,]), 2), list()) == [2]
