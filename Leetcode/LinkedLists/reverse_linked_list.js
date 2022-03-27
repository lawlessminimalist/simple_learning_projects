var reverseList = function(head) {
    let new_head = null;
    while(head != null){
    //store the value of the next node after head
        let nextNode = head.next;
        //set the head next to the new reverse list
        head.next = new_head;
        //set reverse list to current head
        new_head = head;
        //set the head (target val) to the original head.next
        head = nextNode;
    }
    return new_head;
};