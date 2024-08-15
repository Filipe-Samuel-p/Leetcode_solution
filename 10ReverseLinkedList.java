class Solution {
    private void insertionBegin(ListNode head, int data){
        ListNode newNode = new ListNode(data);
        
        if(head.next == null){
            head.next = newNode;
            newNode.next = null;
        }
        else{
            ListNode aux = head.next;
            head.next = newNode;
            newNode.next = aux;
        }

    }
    public ListNode reverseList(ListNode head) {
       
        ListNode reversedList = new ListNode(0,null);

        ListNode aux2 = head;
        while(aux2 != null){
            insertionBegin(reversedList, aux2.val);
            aux2 = aux2.next;
        }

        return reversedList.next;

    }
}