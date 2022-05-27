class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.tail = None

  def enqueue(self, data):
    n = Node(data)
    if not self.head:
      self.head = n
      self.tail = n
    else:
      self.tail.next = n
      self.tail = n

  def dequeue(self):
    res = self.head.data
    self.head = self.head.next
    return res

  def __str__(self):
    res = ''
    curr = self.head
    while curr:
      res += str(curr.data) + " "
      curr = curr.next

    return res


def main():
  # adding nodes to the back and removing from the front
  queue = Queue()
  queue.enqueue(4)
  queue.enqueue(3)
  queue.enqueue(2)
  queue.enqueue(1)
  print(queue)
  queue.dequeue()
  print(queue)


if __name__ == '__main__':
  main()
