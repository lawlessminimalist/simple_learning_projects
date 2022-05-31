class Solution_W2{
public static void main(String[] args) {
    
}

public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
  
 
public static ListNode deleteDuplicates(ListNode head) {
        int last_distinct = -10_000_000;
        ListNode original_list = head;
        int next_val = head.next.val;
        while(head.next!= null){
            //if at start
            if(last_distinct == -10_000_000){
                last_distinct = head.val;
            }
            //check next val
            if(next_val == last_distinct){
                head.next = head.next.next;
                head = head.next;
            }
            else{
                head = head.next;
                if(head.next != null){
                    next_val = head.next.val;
                }
                else{
                    break;
                }
            }

            //if identical change pointer from parent to the next linked list node

            
        }
        return original_list;
}

}

