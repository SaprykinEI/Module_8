import unittest
from main import Node, Stack

class TestNode(unittest.TestCase):

    def test_Node(self):
        node_1 = Node(5)
        self.assertEqual(node_1.data, 5)
        self.assertEqual(node_1.next_node, None)
        node_2 = Node(3, node_1)
        self.assertEqual(node_2.data, 3)
        self.assertEqual(node_2.next_node, node_1)

class TestStack(unittest.TestCase):

    stack = Stack()

    def test_01_init(self):
        self.assertEqual(self.stack.stack_size, 5)
        self.assertEqual(self.stack.top, None)

    def test_02_push(self):
        '''Тестируем заполняемость stack'''

        self.stack.push(1)
        self.stack.push(2)
        self.assertLessEqual(self.stack.size_stack(), self.stack.stack_size)
        self.assertEqual(self.stack.top.data, 2)

    def test_03_pop(self):
        '''Тестируем удаление данных из stack'''


        self.assertTrue(self.stack.top.data)
        self.stack.pop()
        self.assertEqual(self.stack.top.data, 1)
        self.stack.pop()
        self.assertEqual(self.stack.pop(), "Стэк пуст")

    def test_04_is_empty(self):
        '''Тестируем пустой stack'''

        self.stack.push('data_1')
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_05_full(self):
        '''Тестируем метод на полную заполненность stack'''

        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)
        self.assertEqual(self.stack.stack_size, self.stack.size_stack())
        self.assertTrue(self.stack.is_full())
        self.stack.pop()
        self.assertFalse(self.stack.is_full())

    def test_06_clear_stack(self):
        '''Тестируем метод на полную очистку stack'''

        self.assertFalse(self.stack.is_empty())
        self.stack.clear_stack()
        self.assertTrue(self.stack.is_empty())

    def test_07_get_data(self):
        '''Тестируем метод на получение данных по индексу в stack'''

        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.get_data(0), 2)
        self.assertEqual(self.stack.get_data(1), 1)
        self.assertEqual(self.stack.get_data(3), 'Out of range')
        self.assertEqual(self.stack.get_data(-1), 'Out of range')

    def test_08_size_stack(self):
        '''Тестируем размерность stack'''

        self.assertEqual(self.stack.size_stack(), 2)

    def test_09_counter_int(self):
        '''Тестируем метод на подсчет целых чисел в stack'''

        self.stack.push('string')
        self.stack.push(3)
        self.stack.push(3.5)
        self.assertEqual(self.stack.counter_int(), 3)