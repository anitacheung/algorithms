#include <iostream>

using namespace std;


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode();
        ListNode* summed_ptr = head;
        ListNode* ptr1 = l1;
        ListNode* ptr2 = l2;
        int sum = 0;
        
        while ((ptr1 != nullptr) | (ptr2 != nullptr)) {
            // Get sum
            sum = ptr1->val + ptr2->val + summed_ptr->val;
            
            if (sum >= 10) {
                summed_ptr->val = sum - 10;
                summed_ptr->next = new ListNode(1);
            }
            else {
                summed_ptr->val = sum;
            }
            
            // Add empty node
            if ((ptr1->next==nullptr) & (ptr2->next==nullptr)) break;
            else if (ptr1->next == nullptr) ptr1->next = new ListNode();
            else if (ptr2->next == nullptr) ptr2->next = new ListNode();
            
            // Next node
            ptr1 = ptr1->next;
            ptr2 = ptr2->next;
            if (summed_ptr->next == nullptr) {
                summed_ptr->next = new ListNode();
            }
            summed_ptr = summed_ptr->next;
        }
        
        return head;
    }
};