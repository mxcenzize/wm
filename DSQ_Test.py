import unittest
from Deque import Deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):

  def setUp(self):
    self._deque = Deque()
    self._stack = Stack()
    self._queue = Queue()
  
#Deque Tests
  
  def test_empty_deque_string(self):
    self.assertEqual('[ ]', str(self._deque))
  
  def test_nonempty_deque_string(self):
    self._deque.push_front(1)
    self._deque.push_back(2)
    self.assertEqual('[ 1, 2 ]', str(self._deque))
    
  def test_length_empty_deque(self):
    self.assertEqual(0, len(self._deque))
  
  def test_length_nonempty_deque(self):
    self._deque.push_front(5)
    self._deque.push_back(9)
    self.assertEqual(2, len(self._deque))
    self._deque.pop_back()
    self.assertEqual(1, len(self._deque))
  
  def test_push_front_empty_deque(self):
    self._deque.push_front(5)
    self.assertEqual('[ 5 ]', str(self._deque))
    
  def test_push_front_nonempty_deque(self):
    self._deque.push_front(7)
    self._deque.push_front(8)
    self.assertEqual('[ 8, 7 ]', str(self._deque))
    
  def test_pop_front_empty_deque(self):
    try:
      self._deque.pop_front()
      yield self.assertRaises(IndexError)
    finally:
      self.assertEqual('[ ]', str(self._deque))
  
  def test_pop_front_nonempty_deque_five(self):
    self._deque.push_front(1)
    self._deque.push_front(2)
    self._deque.push_front(3)
    self._deque.push_front(4)
    self._deque.push_front(5)
    self._deque.pop_front()
    self.assertEqual('[ 4, 3, 2, 1 ]', str(self._deque))
    
  def test_peek_front_empty_deque(self):
    try:
      self._deque.peek_front()
      yield self.assertRaises(IndexError)
    finally:
      self.assertEqual('[ ]', str(self._deque))
  
  def test_peek_front_nonempty_deque_three(self):
    self._deque.push_front(1)
    self._deque.push_front(2)
    self._deque.push_front(3)
    self.assertEqual(3, self._deque.peek_front())
  
  def test_push_back_empty_deque(self):
    self._deque.push_back(5)
    self.assertEqual('[ 5 ]', str(self._deque))
  
  def test_push_back_nonempty_deque(self):
    self._deque.push_back(1)
    self._deque.push_back(2)
    self._deque.push_back(3)
    self.assertEqual('[ 1, 2, 3 ]', str(self._deque))
  
  def test_pop_back_empty_deque(self):
    try:
      self._deque.pop_back()
      yield self.assertRaises(IndexError)
    finally:
      self.assertEqual('[ ]', str(self._deque))  
  
  def test_pop_back_nonempty_deque(self):
    self._deque.push_front(1)
    self._deque.push_front(2)
    self._deque.push_front(3)
    self._deque.push_front(4)
    self._deque.push_front(5)
    self._deque.pop_back()
    self.assertEqual('[ 5, 4, 3, 2 ]', str(self._deque))
  
  def test_peek_back_empty_deque(self):
    try:
      self._deque.peek_back()
      yield self.assertRaises(IndexError)
    finally:
      self.assertEqual('[ ]', str(self._deque))
        
  def test_peek_back_nonempty_deque_one(self):
    self._deque.push_front(3)
    self.assertEqual(3, self._deque.peek_back())
    
  def test_peek_back_nonempty_deque_three(self):
    self._deque.push_front(1)
    self._deque.push_front(2)
    self._deque.push_front(3)
    self.assertEqual(1, self._deque.peek_back())  

#Queue Tests

  def test_empty_queue_string(self):
    self.assertEqual('[ ]', str(self._queue))
  
  def test_nonempty_queue_string(self):
    self._queue.enqueue(1)
    self._queue.enqueue(3)
    self._queue.enqueue(5)
    self.assertEqual('[ 1, 3, 5 ]', str(self._queue))
  
  def test_len_empty_queue(self):
    self.assertEqual(0, len(self._queue))
  
  def test_len_nonempty_queue(self):
    self._queue.enqueue(10)
    self._queue.enqueue(20)
    self._queue.enqueue(30)
    self.assertEqual(3, len(self._queue))
  
  def test_nonempty_dequeue_queue(self):
    self._queue.enqueue(4)
    self._queue.enqueue(16)
    self._queue.enqueue(64)
    self.assertEqual(3, len(self._queue))
    self.assertEqual('[ 4, 16, 64 ]', str(self._queue))
    self._queue.dequeue()
    self.assertEqual(2, len(self._queue))
    self.assertEqual('[ 16, 64 ]', str(self._queue))
  
  def test_empty_dequeue_queue(self):
    try:
      self._queue.dequeue()
      yield self.assertRaises(IndexError)
    finally:
      self.assertEqual('[ ]', str(self._queue))    

#Stack Tests

  def test_empty_stack_string(self):
    self.assertEqual('[ ]', str(self._stack))
  
  def test_nonempty_stack_string(self):
    self._stack.push(5)
    self._stack.push(10)
    self._stack.push(15)
    self.assertEqual('[ 15, 10, 5 ]', str(self._stack))
  
  def test_empty_stack_len(self):
    self.assertEqual(0 , len(self._stack))
    
  def test_nonempty_stack_len(self):
    self._stack.push(9)
    self._stack.push(18)
    self._stack.push(27)
    self.assertEqual(3, len(self._stack))
  
  def test_push_stack(self):
    self._stack.push(23)
    self._stack.push(24)
    self._stack.push(25)
    self.assertEqual('[ 25, 24, 23 ]', str(self._stack))
    self._stack.push(26)
    self.assertEqual('[ 26, 25, 24, 23 ]', str(self._stack))
  
  def test_empty_stack_pop(self):
    try:
      self._stack.pop()
      yield self.assertRaises(IndexError)
    finally:
      self.assertEqual('[ ]', str(self._stack))
    
  def test_stack_pop(self):
    self._stack.push(100)
    self._stack.push(200)
    self._stack.push(300)
    self.assertEqual('[ 300, 200, 100 ]', str(self._stack))
    self._stack.pop()
    self.assertEqual('[ 200, 100 ]', str(self._stack))
  
  def test_empty_stack_peek(self):
    try:
      self._stack.peek()
      yield self.assertRaises(IndexError)
    finally:
      self.assertEqual('[ ]', str(self._stack))
    
  def test_stack_peek(self):
    self._stack.push(33)
    self._stack.push(44)
    self._stack.push(55)
    self.assertEqual(55, self._stack.peek())
    self._stack.push(66)
    self.assertEqual(66, self._stack.peek())
  
if __name__ == '__main__':
  unittest.main(exit = False)