#include <iostream>
using namespace std;

template <typename T>
class Node {
    public:
        T value;
        Node* next;

        Node(){}
        Node(T value){ this->value = value; }
        ~Node(){}
};

template <typename T>
class LinkedList {
    public:
        Node* head = nullptr;
        Node* tail = nullptr;
        int size = 0;


        LinkedList() {
            this.head = Node();
            this.tail = Node();
        };
        ~LinkedList() {
            Node* curr = this.head->next;
            if (curr) {
                while (curr) {
                    Node* tmp = curr;
                    curr = curr->next;
                    delete tmp;
                }
            }
            delete this.head;
            delete this.tail;
        }
};

int main()
{

    LinkedList<int>* ll = new LinkedList<int>;

    return 0;
}