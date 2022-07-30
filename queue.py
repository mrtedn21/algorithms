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

print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
