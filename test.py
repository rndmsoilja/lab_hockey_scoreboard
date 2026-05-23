import unittest
from main import check_cell, can_display

class TestWhiteBox(unittest.TestCase):
    def test_check_cell_R(self):
        self.assertTrue(check_cell('R', 0))
        self.assertTrue(check_cell('R', 4))
        self.assertTrue(check_cell('R', 7))
        self.assertFalse(check_cell('R', 1))
        self.assertFalse(check_cell('R', 2))
    
    def test_check_cell_G(self):
        self.assertTrue(check_cell('G', 1))
        self.assertTrue(check_cell('G', 5))
        self.assertTrue(check_cell('G', 7))
        self.assertFalse(check_cell('G', 0))
    
    def test_check_cell_B(self):
        self.assertTrue(check_cell('B', 2))
        self.assertTrue(check_cell('B', 6))
        self.assertTrue(check_cell('B', 7))
        self.assertFalse(check_cell('B', 0))
    
    def test_check_cell_dot(self):
        for v in range(8):
            self.assertTrue(check_cell('.', v))
        self.assertFalse(check_cell('.', 8))
    
    def test_can_display_yes(self):
        splash = ["RGB", ".G."]
        board = [[7,7,7],[7,7,7]]
        self.assertTrue(can_display(splash, board))
    
    def test_can_display_no(self):
        splash = ["R"]
        board = [[1]]
        self.assertFalse(can_display(splash, board))

if __name__ == "__main__":
    unittest.main()