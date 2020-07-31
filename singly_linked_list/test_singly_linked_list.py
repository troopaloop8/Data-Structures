import unittest
from singly_linked_list import LinkedList


class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_append(self):
        self.list.append(1)
        self.assertEqual(self.list.tail.value, 1)
        self.assertEqual(self.list.head.value, 1)
        self.list.append(2)
        self.assertEqual(self.list.tail.value, 2)
        self.assertEqual(self.list.head.value, 1)

    def test_contains(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(5)
        self.list.append(10)
        self.assertTrue(self.list.contains(10))
        self.assertTrue(self.list.contains(2))
        self.assertFalse(self.list.contains(1000))

    def test_shift(self):
        self.list.append(10)
        self.list.append(20)
        self.assertEqual(self.list.shift(), 10)
        self.assertFalse(self.list.contains(10))
        self.assertEqual(self.list.shift(), 20)
        self.assertFalse(self.list.contains(20))

        self.list.append(10)
        self.assertEqual(self.list.shift(), 10)
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        self.assertIsNone(self.list.shift())

    def test_get_max(self):
        self.assertIsNone(self.list.get_max())
        self.list.append(100)
        self.assertEqual(self.list.get_max(), 100)
        self.list.append(55)
        self.assertEqual(self.list.get_max(), 100)
        self.list.append(101)
        self.assertEqual(self.list.get_max(), 101)


if __name__ == '__main__':
    unittest.main()
