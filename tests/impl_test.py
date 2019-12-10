import unittest
import impl


class ImplTest(unittest.TestCase):

  def test_hello_world(self):
    result = impl.hello_world()
    self.assertTrue(result.startswith('Hello world'))


if __name__ == '__main__':
  unittest.main()
