from typing import Optional


class Queue:
    def __init__(self) -> None:
        self._list: list[int] = []

    def push(self, item: int) -> None:
        self._list.append(item)

    def pop(self) -> int:
        return self._list.pop(0)


queue = Queue()
queue.push(2)
queue.push(7)
queue.push(1)
queue.push(6)

print('Result of easy queue')
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())


class ListItem:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.following: Optional["ListItem"] = None


class CustomQueue:
    def __init__(self) -> None:
        self._root: Optional[ListItem] = None
        self._head: Optional[ListItem] = None

    def push(self, value: int) -> None:
        if not self._root:
            self._root = ListItem(value)
            self._head = self._root
        else:
            new_item: ListItem = ListItem(value)
            self._head.following = new_item
            self._head = new_item

    def pop(self) -> int:
        value: int = self._root.value
        self._root = self._root.following
        return value


queue = CustomQueue()
queue.push(2)
queue.push(7)
queue.push(1)
queue.push(6)

print('Result of custom queue')
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
