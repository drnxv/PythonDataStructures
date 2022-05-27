# this is an implementation of a doubly linked list
# it has a reference to the node in front of it and behind

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        to_add = Node(data)
        if not self.head:
            self.head = to_add
            self.tail = to_add
        else:
            self.tail.next = to_add
            self.tail = to_add

    def remove_node(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
        else:
            curr = self.head
            behind = None
            while curr:
                if curr.data == data:
                    behind.next = curr.next
                    curr.prev = behind

                behind = curr
                curr = curr.next

    def __str__(self):
        res = ''
        curr = self.head
        while curr:
            res += str(curr.data) + ' '
            curr = curr.next

        return res


def main():
    nums = List()
    nums.add_node(5)
    nums.add_node(4)
    nums.add_node(3)
    nums.add_node(2)
    print(nums)
    nums.remove_node(4)
    print(nums)
    nums.remove_node(5)
    print(nums)


if __name__ == '__main__':
    main()
