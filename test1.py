import unittest, prog1

class SquareEqSolverTestCase(unittest.TestCase):
    def correct_sort_b(self):
        res = prog1.bubble_sort([8, 3, 1, 5])
        self.assertEqual(res, [1, 3, 5, 8])

    def correct_sort_q(self):
        res = prog1.quicksort([8, 3, 1, 5])
        self.assertEqual(res, [1, 3, 5, 8])
        
    def correct_sort_s(self):
        res = prog1.selection_sort([8, 3, 1, 5])
        self.assertEqual(res, [1, 3, 5, 8])

    