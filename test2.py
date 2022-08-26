import unittest
import script

class TestGane(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = script.run_guess(answer,guess)
        self.assertEqual(result)


if __name__ == '__main__':
    unittest.main()


