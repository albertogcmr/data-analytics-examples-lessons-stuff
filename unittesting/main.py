import unittest
from functions import suma
from random import randint

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestSuma(unittest.TestCase): 

    def _suma_test(self, a, b): 
        return a + b

    def test_suma(self): 
        a = 10
        b = 12
        self.assertEqual(suma(a, b), self._suma_test(a, b))


class TestSuma2(unittest.TestCase): 

    def _suma_test(self, a, b): 
        return a + b

    def test_multiple_suma(self): 
        for _ in range(100): 
            a = randint(-100, 100)
            b = randint(-100, 100)
            self.assertEqual(suma(a, b), self._suma_test(a, b))

if __name__ == '__main__':
    unittest.main()