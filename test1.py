import unittest, time 
import prog1

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

    def correct_time_b(self):
        t1 = time.time()
        res = prog1.bubble_sort([8, 3, 1, 5])
        t2 = time.time()
        self.assertEqual(t2 - t1, 4)

    def correct_time_q(self):
        t1 = time.time()
        res = prog1.quicksort([8, 3, 1, 5])
        t2 = time.time()
        self.assertEqual(t2 - t1, 4)
        
    def correct_time_s(self):
        t1 = time.time()
        res = prog1.selection_sort([8, 3, 1, 5])
        t2 = time.time()
        self.assertEqual(t2 - t1, 4)