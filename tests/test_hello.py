import unittest
from desoper import devops_test


class Test_hello(unittest.TestCase):
    def test__working(self):
        self.assertEqual(devops_test.hello(),
                         'Hi, World!', True)


if __name__ == '__main__':
    unittest.main()
