/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
 var removeNthFromEnd = function(head, n) {
    //naive approach
    //edge cases if array of size 1 or empty
    if(head.next === null || head ===null){
        return null;
    }
    
    //loop through linked list to find length
    let size = 0;
    let temp = head;
    while(temp != null){
        size +=1;
        temp = temp.next;
    }
    //loop through a second time and remove the value from linkedlist
    target = size - n;
    //edge case if removing head
    if(target === 0){
        head = head.next;
        return head;
    }

    let count = 1;
    temp = head;
    while(temp != null){
        if(count === target){
            temp.next = temp.next.next;
            return head;
        }
        temp = temp.next;
        count +=1;
    }
    //return head
};