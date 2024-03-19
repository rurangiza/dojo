#ifndef CONTAINERS_H
    #define CONTAINERS_H

    #include <stdio.h>
    #include <stdlib.h>
    #include <stdbool.h>

    typedef struct Vector {
        int     size;
        int     capacity;
        int*    container;
        int     (*get_size)(struct Vector*);
        int     (*get_capacity)(struct Vector*);
        bool    (*is_empty)(struct Vector*);
        int     (*at)(struct Vector*, int index);
        void    (*resize)(struct Vector*);
        void    (*append)(struct Vector*, int number);
        void    (*prepend)(struct Vector*, int number);
        void    (*insert)(struct Vector*, int number, int index);
        int     (*pop)(struct Vector*);
        void    (*delete)(struct Vector*, int number);
        void    (*remove)(struct Vector*, int number);
        int     (*find)(struct Vector*, int number);
    }   Vector;

    

#endif // CONTAINERS_H