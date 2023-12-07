import unittest
from stack import Stack
from script import TowersOfHanoi

class TestTowersOfHanoi(unittest.TestCase):

    def test_init(self):
        hanoi = TowersOfHanoi(3)
        self.assertEqual(hanoi.num_disks, 3)
        self.assertEqual(hanoi.num_optimal_moves, 7)
        self.assertIsInstance(hanoi.left_stack, Stack)
        self.assertIsInstance(hanoi.middle_stack, Stack)
        self.assertIsInstance(hanoi.right_stack, Stack)

    def test_setup_game(self):
        hanoi = TowersOfHanoi(3)
        hanoi.setup_game()
        self.assertEqual(hanoi.left_stack.get_size(), 3)

    def test_valid_move_disk(self):
        hanoi = TowersOfHanoi(3)
        hanoi.setup_game()

        # Move disk from left to middle
        hanoi.move_disk(hanoi.left_stack, hanoi.middle_stack)
        self.assertEqual(hanoi.middle_stack.peek(), 0)
        self.assertEqual(hanoi.num_user_moves, 1)

    def test_invalid_move_disk(self):
        hanoi = TowersOfHanoi(3)
        hanoi.setup_game()

        # Moving disk from empty stack
        with self.assertRaises(SystemExit):
            hanoi.move_disk(hanoi.middle_stack, hanoi.right_stack)

        # Placing larger disk on top of smaller disk
        hanoi.move_disk(hanoi.left_stack, hanoi.middle_stack)
        with self.assertRaises(SystemExit):
            hanoi.move_disk(hanoi.left_stack, hanoi.middle_stack)

    def test_check_game_over(self):
        hanoi = TowersOfHanoi(3)
        hanoi.setup_game()

        # Not yet game over
        hanoi.check_game_over()
        self.assertEqual(hanoi.right_stack.get_size(), 0)

        # Now move disks to make game over
        hanoi.move_disk(hanoi.left_stack, hanoi.right_stack)
        hanoi.move_disk(hanoi.left_stack, hanoi.middle_stack)
        hanoi.move_disk(hanoi.right_stack, hanoi.middle_stack)
        hanoi.move_disk(hanoi.left_stack, hanoi.right_stack)
        hanoi.move_disk(hanoi.middle_stack, hanoi.left_stack)
        hanoi.move_disk(hanoi.middle_stack, hanoi.right_stack)
        hanoi.move_disk(hanoi.left_stack, hanoi.right_stack)

        hanoi.check_game_over()
        self.assertEqual(hanoi.right_stack.get_size(), 3)

if __name__ == '__main__':
    unittest.main()
