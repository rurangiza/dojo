#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/*
 * Implement a vector (mutable array with automatic resizing):
*/

typedef struct Vector {
    int     size;
    int     capacity;
    int*    container;
    int     (*get_size)(struct Vector*);
    int     (*get_capacity)(struct Vector*);
    bool    (*is_empty)(struct Vector*);
    int     (*at)(struct Vector*, int);
    void    (*resize)(struct Vector*);
    void    (*append)(struct Vector*, int);
    void    (*prepend)(struct Vector*, int);
    void    (*insert)(struct Vector*, int, int);
    int     (*pop)(struct Vector*);
    void    (*delete)(struct Vector*, int);
    void    (*remove)(struct Vector*, int);
    int     (*find)(struct Vector*, int);
}   Vector;

int get_size(Vector* self)
{
    return self->size;
}

int get_capacity(Vector* self)
{
    return self->capacity;
}

bool is_empty(Vector* self)
{
    if (self->size == 0)
        return true;
    return false;
}

int at(Vector* self, int index)
{
    if (index >= 0 && index < self->size)
        return self->container[index];
    return -1;
}

void resize(Vector* self)
{
    int* newContainer = NULL;

    if (self == NULL)
        return ;

    self->capacity *= 2;
    newContainer = calloc(self->capacity, sizeof(int));
    for (int offset = 0; offset < self->size; offset++)
    {
        *(newContainer + offset) = *(self->container + offset);
    }
    free(self->container);
    self->container = newContainer;
}

void append(Vector* self, int num)
{
    if (self->size == self->capacity)
    {
        self->resize(self); // O(2*N)
    }
    *(self->container + self->size) = num; // O(1)
    self->size++; // O(1)
}

void insert(Vector* self, int num, int idx)
{
    if (idx < 0) idx = 0;
    if (idx > self->size)
    {
        self->append(self, num);
        return ;
    }
    if (self->size == self->capacity) self->resize(self);

    for (int offset = self->size-1; offset >= idx; offset--)
    {
        *(self->container + offset + 1) = *(self->container + offset);
        if (offset == idx)
        {
            *(self->container + offset) = num;
            break ;
        }
    }
    self->size++;
}

void prepend(Vector* self, int num)
{
    self->insert(self, num, 0);
}

// remove from end, return value
int pop(Vector* self)
{
    if (self->is_empty(self))
        return -1;
    
    self->size--;
    return *(self->container + self->size);
}

// delete item at index, shifting all trailing elements left
void delete(Vector* self, int idx)
{
    if (self->is_empty(self) || idx < 0 || idx >= self->size)
        return ;

    while (idx < self->size-1)
    {
        *(self->container + idx) = *(self->container + idx + 1);
        idx++;
    }
    self->size--;
}

// looks for value and removes index holding it (even if in multiple places)
void remove_fn(Vector* self, int target)
{
    int count = 0, insert_pos = 0;
    int* newContainer = NULL;

    // count
    for (int offset = 0; offset < self->size; offset++)
    {
        if (*(self->container + offset) == target)
            count++;
    }
    // allocate
    newContainer = calloc(self->size - count, sizeof(int));
    if (newContainer == NULL)
        return ;
    // copy
    for (int offset = 0; offset < self->size; offset++)
    {
        if (*(self->container + offset) != target)
            *(newContainer + insert_pos) = *(self->container + offset);
    }
    free(self->container);
    self->container = newContainer;
}

// looks for value and returns first index with that value, -1 if not found
int find(Vector* self, int target)
{
    if (self == NULL)
        return -1;

    for (int offset = 0; offset < self->size; offset++)
    {
        if (*(self->container + offset) == target)
            return offset;
    }
    return -1;
}

Vector* newVector()
{
    Vector* v = calloc(1, sizeof(Vector));

    v->size = 0;
    v->capacity = 4;
    v->container = calloc(v->capacity, sizeof(int));
    v->get_size = get_size;
    v->get_capacity = get_capacity;
    v->is_empty = is_empty;
    v->at = at;
    v->append = append;
    v->prepend = prepend;
    v->insert = insert;
    v->resize = resize;
    v->pop = pop;
    v->remove = remove_fn;
    v->delete = delete;
    v->find = find;
    return v;
}

int main()
{
    Vector* v = newVector();
    
    printf("Size: %d\n", v->get_size(v));
    printf("Capacity: %d\n", v->get_capacity(v));

    v->append(v, 45);
    v->append(v, 65);
    v->append(v, 100);
    v->append(v, 9);
    v->append(v, 999);
    v->insert(v, 1188, 40);

    for (int i = 0; i < v->get_size(v); i++)
    {
        printf("[%d] %d\n", i, *(v->container + i));
    }

    printf("Size: %d\n", v->get_size(v));
    printf("Capacity: %d\n", v->get_capacity(v));

    free(v->container); free(v);
    return 0;
}