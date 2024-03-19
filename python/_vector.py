from typing import List

class Vector:
    def __init__(self, items: List[int]=[]) -> None:
        self._size = len(items)
        self._capacity = (len(items)+1) * 2
        self._container = [0] * self._capacity
        for i, x in enumerate(items):
            self._container[i] = x
    
    # occupied space
    def size(self) -> int:
        return self._size

    # allocated space
    def capacity(self) -> int:
        return self._capacity

    # check if vector is empty
    def is_empty(self) -> bool:
        if self.size == 0:
            return True
        return False

    # return num at specific index
    def at(self, idx: int) -> int:
        if idx < 0 or idx >= self._size:
            return None
        return self._container[idx]

    # increase/decrease capacity based on size
    def _resize(self) -> None:
        if self._size == self._capacity:
            self._capacity *= 2
        elif self._size <= self._capacity // 4:
            self._capacity /= 2
        
        newArr = [0] * self._capacity
        for i in range(self._size):
            newArr[i] = self._container[i]
        self._container = newArr
    
    # insert at end
    def append(self, num: int) -> None:
        if self._size == self._capacity:
            self._resize()
        self._container[self._size] = num
        self._size += 1

    # insert at begining
    def prepend(self, num: int) -> None:
        self.insert(num, 0)

    # insert num at specific index
    def insert(self, num: int, idx: int) -> None:
        if idx > self._size:
            return
        if self._size == self._capacity:
            self._resize()

        for i in range(self._size, idx-1, -1):
            if i == idx:
                self._container[i] = num
                break
            self._container[i] = self._container[i-1]
        self._size += 1

    # remove and return last num
    def pop(self):
        if self._size > 0:
            self._size -= 1
            return self._container[self._size]
        return None

    # delete item at index, shifting all trailing elements left
    def delete(self, index: int):
        if self.is_empty():
            return
    
        for i in range(index, len(self._container)-1):
            self._container[i] = self._container[i+1]
        self._size -= 1

    # // looks for value and removes index holding it (even if in multiple places)
    def remove(self, target: int) -> None:
        new_size = self._size - self._container.count(target)
        tmp, pos = [0] * self._capacity, 0


        for i in range(self._size):
            if self._container[i] != target:
                tmp[pos] = self._container[i]
                pos += 1
        self._container = tmp

        self._size = pos

        """ or
            v = self._container
            tmp = [v[i] for i in range(self._size) if v[i] != target]
            self._container = v
            self._size = len(tmp)
        """
        
    # looks for value and returns first index with that value, -1 if not found
    def find(self, num: int) -> int:
        for i, n in enumerate(self._container):
            if n == num:
                return i

    def __repr__(self) -> str:
        return f'Vector of size: {self._size} and capacity {self._capacity}:\n{self._container[:self._size]}'

if __name__ == '__main__':
    v = Vector([1, 2, 3])
    v.append(4)
    v.append(6)
    v.insert(5, 4)
    v.pop()
    v.insert(6, 5)
    v.append(2)
    v.append(2)
    v.append(7)
    v.remove(2)
    v.insert(2, 1)
    v.find(3)
    v.delete(0)
    print(f'capacity: {v.capacity()}')
    print(f'size: {v.size()}')
    print(v)
    
