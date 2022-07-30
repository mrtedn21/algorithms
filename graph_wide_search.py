from my_queue import Queue


class NotFound(Exception):
    pass


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.friends: dict[str, Person] = {}


def wide_search(first_element: Person, searching_age: int) -> Person:
    queue: Queue = Queue()
    checked_people: list[Person] = []

    queue.push_many(*first_element.friends.values())
    while not queue.is_empty():
        new_element: Person = queue.pop()
        if new_element.age == searching_age:
            return new_element
        checked_people.append(new_element)
        for element in new_element.friends.values():
            if element not in checked_people:
                queue.push(element)

    raise NotFound('Searching age not found')


sasha: Person = Person('sasha', 23)
ulya: Person = Person('ulya', 20)
vet: Person = Person('vet', 24)

sasha.friends['ulya'] = ulya
sasha.friends['vet'] = vet

dasha: Person = Person('dasha', 19)
ulya.friends['dasha'] = dasha

found_friend: Person = wide_search(sasha, 19)
print(f'Found friend with age 19 is {found_friend.name}')
