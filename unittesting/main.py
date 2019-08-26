import unittest

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

# importada desde fuera por ejemplo
def suma(a, b): 
    return a + b

class TestViking(unittest.TestCase): 

    def _suma_test(self, a, b): 
        return a + b

    def test_viking(self): 
        a = 10
        b = 12
        self.assertEqual(suma(a, b), self._suma_test(a, b))

if __name__ == '__main__':
    unittest.main()