"""
Demonstrates two approaches for creating data-centric classes in Python:

1. ManualComment:
   - Traditional class with manually implemented methods
     (__init__, __repr__, __eq__, ordering, hashing).
   - Illustrates the amount of boilerplate required.

2. Comment (@dataclass):
   - Uses Python's dataclasses module to automatically generate
     common methods.
   - Demonstrates immutability (frozen=True), ordering (order=True),
     field customization, serialization, and object copying.
"""


import dataclasses
import inspect
from dataclasses import dataclass, field
from pprint import pprint       # = "pretty print"


class ManualComment:
    def __init__(self, id: int, text: str):
        self.id: int = id
        self.text: str = text

    def __repr__(self):
        return "{}(id={}, text={})".format(self.__class__.__name__, self.id, self.text)

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) == (other.id, other.text)
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result

    def __hash__(self):
        return hash((self.__class__, self.id, self.text))

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) < (other.id, other.text)
        else:
            return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) <= (other.id, other.text)
        else:
            return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) > (other.id, other.text)
        else:
            return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) >= (other.id, other.text)
        else:
            return NotImplemented


@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str = ""
    replies: list[int] = field(default_factory=list, repr=False, compare=False)


def main():
    comment = Comment(1, "I just subscribed!")
    # comment.id = 3  # can't immutable
    print(comment)
    print(dataclasses.astuple(comment))
    print(dataclasses.asdict(comment))
    copy = dataclasses.replace(comment, id=3)
    print(copy)

    pprint(inspect.getmembers(Comment, inspect.isfunction))


if __name__ == '__main__':
    main()