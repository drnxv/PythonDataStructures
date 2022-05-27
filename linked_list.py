# this is going to be a linked list implementation in python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = new_node

    def remove_node(self, data):
        curr = self.head
        prev = None

        # special case if the head needs to be removed
        if self.head.data == data:
            self.head = self.head.next
        else:
            while curr:
                if curr.data == data:
                    prev.next = curr.next

                prev = curr
                curr = curr.next

    # clear the linked list
    def reset(self):
        self.head = None

    # to string method
    def __str__(self):
        res = ''
        curr = self.head
        while curr:
            res += str(curr.data) + ' '
            curr = curr.next

        return res

def main():
    nums = List()
    nums.add(3)
    nums.add(2)
    nums.add(1)
    nums.remove_node(3)
    print(nums)

if __name__ == '__main__':
    main()
