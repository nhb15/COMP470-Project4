import unittest

class ServiceTest(unittest.TestCase):

    def testPlus(self):
        # mockito.when(service.plus(2, 2)).thenReturn(4)
        # out = mockito.mock()
        # ArgumentCaptor
        # service.plus(out)
        #
        # verify(out).write(4)
        # assert(service.plus(2, 2) == 4)
        self.assertEqual(plus(2, 2), 4, "test")

    def test_minus(self):
        # out = mock()
        #
        # service.minus(out)
        self.assertEqual(minus(2, 2), 0)
        # assert(service.minus(2, 2) == 0)

    # def test_multiply(self):
    #     # out = mock()
    #
    #     assert(service.multiply(2, 2) == 4)
    #
    # def test_divide(self):
    #     # out = mock()
    #
    #     assert(service.divide(2, 2) == 1)

def plus(number1, number2):
    return int(number1) + int(number2)

def minus(number1, number2):
    return int(number1) - int(number2)

def multiply(number1, number2):
    return int(number1) * int(number2)

def divide(number1, number2):
    return int(number1) / int(number2)