

class Solution {

    private void insertNode(ListNode head, int data){

        ListNode newNode = new ListNode(data,null);
        if(head.next == null){
            head.next = newNode;
        }
        else{
            ListNode aux = head.next;
            while(aux.next != null){
                aux = aux.next;
            }
            aux.next = newNode;
        }
    }

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        ListNode list3 = new ListNode(0, null);

        while(!(list1 == null && list2 == null)){
            
            if(list1 != null && list2 == null){
                insertNode(list3, list1.val);
                list1 = list1.next;
            } 
            else if(list1 == null && list2 != null){
                insertNode(list3, list2.val);
                list2 = list2.next;
            }
            else{

                if(list1.val > list2.val){
                    insertNode(list3, list2.val);
                    list2 = list2.next;
                }
                else if(list1.val == list2.val){
                    insertNode(list3, list1.val);
                    insertNode(list3, list2.val);
                    list1 = list1.next;
                    list2 = list2.next;
                }
                else{
                    insertNode(list3, list1.val);
                    list1 = list1. next;
                } 
            }
        }

        return list3.next;
    }
}