
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode newHead = new ListNode(0);
        ListNode Curr = newHead;
        while (list1 != null && list2 != null){
            if(list1.val < list2.val ){
                Curr.next = list1;
                list1 = list1.next;}
            else {
                Curr.next = list2;
                list2 = list2.next;
            }
            Curr = Curr.next;

        }
        if (list2 == null){
            Curr.next = list1;
        }
        if (list1 == null){
            Curr.next = list2;
        }
        return newHead.next;
        
    } 
}