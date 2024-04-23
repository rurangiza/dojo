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

// remove the front item and return its value
int pop_front(LinkedList* ll)
{
    if (!ll || ll->size == 0)
        return -1;
    
    Node* old_front = ll->head->next;
    Node* new_front = old_front->next;

    ll->head->next = new_front;

    int result = old_front->value;
    free(old_front);
    ll->size--;

    return result;
}

// adds an item at the end
void push_back(int value, LinkedList* ll)
{
    if (!ll)
        return ;
    
    Node* new = newNode(value);

    if (!ll->head->next)
    {
        ll->head->next = new;
        ll->tail->next = new;
    }
    else
    {
        ll->tail->next->next = new;
        ll->tail->next = new;
    }
    ll->size++;
}

// removes end item and returns its value
int pop_back(LinkedList* ll)
{
    if (!ll || ll->size == 0)
        return -1;
    
    Node* curr = ll->head;
    while (curr->next != ll->tail->next)
        curr = curr->next;
    
    ll->tail->next = curr;
    Node* popped_node = curr->next;
    curr->next = NULL;
    ll->size--;

    int popped_val = popped_node->value;
    free(popped_node);

    return popped_val;
}


// get the value of the front item
int front(LinkedList* ll)
{
    if (!ll || ll->size == 0)
        return -1;
    return ll->head->next->value;
}

// get the value of the end item
int back(LinkedList* ll)
{
    if (!ll || ll->size == 0)
        return -1;
    return ll->tail->next->value;
}

// insert value at index, so the current item at that index is pointed to by the new item at the index
void insert_node(int index, int value, LinkedList* ll)
{
    if (!ll || index < 0 || index > ll->size)
        return ;
    
    Node* prev = ll->head;
    int count = 0;
    while (prev && count < index)
    {
        prev = prev->next;
        count++;
    }
    Node* next = prev->next;
    
    Node* new = newNode(value);
    new->next = next;
    prev->next = new;

    if (index == ll->size)
        ll->tail->next = new;
    ll->size++;
}

// removes node at given index
void erase(int index, LinkedList* ll)
{
    if (!ll || index < 0 || index >= ll->size)
        return ;
    
    Node* prev = ll->head;
    int count = 0;
    while (prev && count < index)
    {
        count++;
        prev = prev->next;
    } 
    Node* target = prev->next;
    Node* next = target->next;
    prev->next = next;

    free(target);

    if (index == ll->size-1)
        ll->tail->next = next;
    ll->size--;
}

// returns the value of the node at the nth position from the end of the list
int at_index(int index, LinkedList* ll)
{
    if (!ll || index < 0 || index >= ll->size)
        return -1;
    
    Node* curr = ll->head->next;
    int count = 0;
    while (curr && count < index)
    {
        count++;
        curr = curr->next;
    }
    if (curr)
        return curr->value;
    return -1;
}

// reverses the list
void reverse(LinkedList* ll)
{
    if (!ll || ll->size <= 1)
        return ;
    
    Node* curr = ll->head->next;
    Node* prev = NULL;
    Node* next = NULL;
    while (curr)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    Node* tmp = ll->tail->next;
    ll->tail->next = ll->head->next;
    ll->head->next = tmp;
}

// removes the first item in the list with this value
void remove_value(int value, LinkedList* ll)
{
    if (!ll || ll->size == 0)
        return ;
    
    Node* curr = ll->head;
    while (curr->next && curr->next->value != value)
        curr = curr->next;
    if (curr->next)
    {
        Node* target = curr->next;
        Node* next = target->next;
        curr->next = next;
        if (ll->tail->next == target)
            ll->tail->next = curr;
        free(target);
    }
}

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
    LinkedList* ll = newLinkedList();
    int res(void);

    push_front(11, ll);
    push_front(22, ll);
    push_front(150, ll);
    
    print_list(ll);

    free_list(ll);
    return 0;
}