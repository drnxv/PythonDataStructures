# this is an implementation of a stack using a linked list
class Node:
  def __init__(self, data=None):
    self.next = None
    self.data = data


class Stack:
  def __init__(self):
    self.head = None

  def push_node(self, data):
    n = Node(data)
    if not self.head:
      self.head = n
    else:
      curr = self.head
      while curr.next:
        curr = curr.next

      curr.next = n

  def pop_node(self):
    curr = self.head
    while curr.next.next:
      curr = curr.next

    last = curr.next
    res = last.data
    curr.next = None 
    last = None
    return res

  def is_empty(self) -> bool:
    return self.head is None

  def __str__(self):
    curr = self.head
    res = ''
    while curr:
      res += str(curr.data) + ' '
      curr = curr.next

    return res


def main():
  stack = Stack()
  stack.push_node(12)
  stack.push_node(45)
  stack.push_node(78)
  stack.push_node(11)
  stack.push_node(90)
  print(stack)
  print(stack.pop_node())
  print(stack)


if __name__ == '__main__':
  main()
