#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
    int value;
    struct Node* next;
}   Node;

typedef struct LinkedList {
    Node* head;
    Node* tail;
    int size;
}   LinkedList;

// --------

Node* newNode(int value)
{
    Node* n = malloc(sizeof(Node));
    if (!n)
        return NULL;
    n->value = value;
    n->next = NULL;
    return n;
}

LinkedList* newLinkedList()
{
    LinkedList* ll = malloc(sizeof(LinkedList));
    if (!ll)
        return NULL;
    ll->head = newNode(-1);
    ll->tail = newNode(-1);
    ll->size = 0;
    return ll;
}

// returns the number of data elements in the list
int list_size(LinkedList* ll)
{
    if (!ll)
        return -1;
    return ll->size;
}

// returns true if empty
bool empty(LinkedList* ll)
{
    if (!ll || ll->size == 0)
        return true;
    return false;
}

// returns the value of the nth item (starting at 0 for first)
int value_at(int index, LinkedList* ll)
{
    if (!ll || index >= ll->size)
        return -1;
    
    Node* curr = ll->head->next;
    if (!curr)
        return -1;

    int count = 0;
    while (curr && count != index)
        curr = curr->next;
    return curr->value;
}

// adds an item to the front of the list
void push_front(int value, LinkedList* ll)
{
    if (!ll)
        return ;
    
    Node* curr = ll->head->next;
    Node* new = newNode(value);
    if (!new)
        return ;

    if (!curr)
    {
        ll->head->next = new;
        ll->tail->next = new;
    }
    else
    {
        new->next = ll->head->next;
        ll->head->next = new;
    }
    ll->size++;
}

/*
// remove the front item and return its value
int pop_front(LinkedList* ll)
{
    ;
}

// adds an item at the end
void push_back(int value, LinkedList* ll)
{
    ;
}

// removes end item and returns its value
int pop_back(LinkedList* ll)
{
    ;
}

// get the value of the front item
int front(LinkedList* ll)
{
    ;
}

// get the value of the end item
int back(LinkedList* ll)
{
    ;
}

// insert value at index, so the current item at that index is pointed to by the new item at the index
void insert(int index, int value, LinkedList* ll)
{
    ;
}

// removes node at given index
void erase(int index, LinkedList* ll)
{
    ;
}

// returns the value of the node at the nth position from the end of the list
int at_index(int n, LinkedList* ll)
{
    ;
}

// reverses the list
void reverse(LinkedList* ll)
{
    ;
}

// removes the first item in the list with this value
void remove_value(int value, LinkedList* ll)
{
    ;
}

*/

void print_list(LinkedList* ll)
{
    Node* curr = ll->head->next;
    if (!curr)
    {
        printf("Empty list\n");
        return ;
    }
    while (curr)
    {
        printf("[%d] -> ", curr->value);
        curr = curr->next;
    }
    printf("\n");
}

void free_list(LinkedList* ll)
{
    Node* curr = ll->head->next;

    if (curr)
    {
        while (curr)
        {
            Node* tmp = curr;
            curr = curr->next;
            free(tmp);
        }
    }
    free(ll->head);
    free(ll->tail);
    free(ll);
}

int main()
{

    LinkedList* a = newLinkedList();

    print_list(a);

    push_front(11, a);
    push_front(22, a);
    push_front(33, a);

    print_list(a);

    free_list(a);
    return 0;
}