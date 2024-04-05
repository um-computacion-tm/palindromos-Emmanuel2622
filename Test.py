from Palindromos import is_palindrome
import unittest

class TestPalindrome(unittest.TestCase):
    def test_1(self):
        result = is_palindrome("aca")
        self.assertEqual(result, True)

    def test_2(self):
        result = is_palindrome("a")
        self.assertEqual(result, True)

    def test_3(self):
        result = is_palindrome("abca")
        self.assertEqual(result, False)
        
    def test_4(self):
        result = is_palindrome("neuquen")
        self.assertEqual(result, True)

    def test_5(self):
        result = is_palindrome("hola")
        self.assertEqual(result, False)
    
    def test_6(self):
        result = is_palindrome("ana")
        self.assertEqual(result, True)

    def test_7(self):
        result = is_palindrome("pop")
        self.assertEqual(result, True)

    def test_8(self):
        result = is_palindrome("pepe pepe")
        self.assertEqual(result, False)

    def test_9(self):
        result = is_palindrome("ana amaana")
        self.assertEqual(result, True)

    def test_10(self):
        result = is_palindrome("ojo corre poco perro cojo")
        self.assertEqual(result, True)

    def test_11(self):
        result = is_palindrome("ojo ojo")
        self.assertEqual(result, True)    
unittest.main()