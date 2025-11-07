import unittest
import os
from io import StringIO
import sys

# Import the functions to test
# Assuming the solution is in a file called 'solution.py'
from main import (
    draw_square,
    draw_number_triangle,
    factorial,
    bar_graph,
    pascals_triangle
)


class TestDrawSquare(unittest.TestCase):
    """Test cases for draw_square function"""
    
    def test_small_filled_square(self):
        """Test a small 3x3 filled square"""
        result = draw_square(3, filled=True)
        expected = "***\n***\n***\n"
        self.assertEqual(result, expected)
    
    def test_small_hollow_square(self):
        """Test a small 3x3 hollow square"""
        result = draw_square(3, filled=False)
        expected = "***\n* *\n***\n"
        self.assertEqual(result, expected)
    
    def test_larger_hollow_square(self):
        """Test a 5x5 hollow square"""
        result = draw_square(5, filled=False)
        expected = "*****\n*   *\n*   *\n*   *\n*****\n"
        self.assertEqual(result, expected)
    
    def test_custom_character(self):
        """Test square with custom character"""
        result = draw_square(3, filled=True, char="#")
        expected = "###\n###\n###\n"
        self.assertEqual(result, expected)
    
    def test_size_one(self):
        """Test edge case: size 1"""
        result = draw_square(1, filled=False)
        expected = "*\n"
        self.assertEqual(result, expected)
    
    def test_size_two_hollow(self):
        """Test edge case: size 2 hollow"""
        result = draw_square(2, filled=False)
        expected = "**\n**\n"
        self.assertEqual(result, expected)

class TestDrawNumberTriangle(unittest.TestCase):
    """Test cases for draw_number_triangle function"""
    
    def test_height_four(self):
        """Test the example case from docstring"""
        result = draw_number_triangle(4)
        expected = "\n1 \n2 3 \n4 5 6 \n"
        self.assertEqual(result, expected)
    
    def test_height_one(self):
        """Test edge case: height 1"""
        result = draw_number_triangle(1)
        expected = "\n"
        self.assertEqual(result, expected)
    
    def test_height_five(self):
        """Test height 5"""
        result = draw_number_triangle(5)
        expected = "\n1 \n2 3 \n4 5 6 \n7 8 9 10 \n"
        self.assertEqual(result, expected)
    
    def test_line_count(self):
        """Test that the number of lines matches height"""
        result = draw_number_triangle(6)
        lines = result.split('\n')
        # Should have height + 1 lines (including final newline)
        self.assertEqual(len(lines), 7)


class TestFactorial(unittest.TestCase):
    """Test cases for factorial function"""
    
    def test_factorial_zero(self):
        """Test 0! = 1"""
        self.assertEqual(factorial(0), 1)
    
    def test_factorial_one(self):
        """Test 1! = 1"""
        self.assertEqual(factorial(1), 1)
    
    def test_factorial_five(self):
        """Test 5! = 120"""
        self.assertEqual(factorial(5), 120)
    
    def test_factorial_ten(self):
        """Test 10! = 3628800"""
        self.assertEqual(factorial(10), 3628800)
    
    def test_factorial_three(self):
        """Test 3! = 6"""
        self.assertEqual(factorial(3), 6)
    
    def test_factorial_seven(self):
        """Test 7! = 5040"""
        self.assertEqual(factorial(7), 5040)


class TestBarGraph(unittest.TestCase):
    """Test cases for bar_graph function"""
    
    def setUp(self):
        """Create a test grades.txt file before each test"""
        self.test_file = "grades_test.txt"
        with open(self.test_file, "w") as f:
            f.write("75, 82, 78, 85, 80, 76, 83, 79, 81, 84, 77, 80, 82, 78, 80\n")
            f.write("28, 32, 30, 25, 35, 28, 31, 29, 33, 27, 30, 32, 28, 31, 31\n")
            f.write("58, 62, 60, 55, 65, 58, 61, 59, 63, 57, 60, 62, 58, 61, 61\n")
            f.write("68, 72, 70, 65, 75, 68, 71, 69, 73, 67, 70, 72, 68, 71, 71\n")
            f.write("78, 82, 80, 75, 85, 78, 81, 79, 83, 77, 80, 82, 78, 81, 81\n")
            f.write("88, 92, 90, 85, 95, 88, 91, 89, 93, 87, 90, 92, 88, 91, 91\n")
            f.write("8, 12, 10, 5, 15, 8, 11, 9, 13, 7, 10, 12, 8, 11, 11\n")
            f.write("18, 22, 20, 15, 25, 18, 21, 19, 23, 17, 20, 22, 18, 21, 21\n")
    
    def tearDown(self):
        """Remove the test file after each test"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_bar_graph_format(self):
        """Test that bar graph returns proper format"""
        result = bar_graph()
        self.assertTrue(result.startswith("Class averages:\n"))
    
    def test_bar_graph_line_count(self):
        """Test that bar graph has correct number of lines"""
        result = bar_graph()
        lines = result.strip().split('\n')
        # Should have header + 8 classes
        self.assertEqual(len(lines), 9)
    
    def test_bar_graph_contains_stars(self):
        """Test that bar graph contains asterisks"""
        result = bar_graph()
        self.assertIn("*", result)
    
    def test_bar_graph_class_labels(self):
        """Test that classes are numbered correctly"""
        result = bar_graph()
        for i in range(1, 9):
            self.assertIn(f"{i}:", result)
    
    def test_bar_graph_average_80(self):
        """Test that class with average 80 shows 8 stars"""
        result = bar_graph()
        lines = result.split('\n')
        # First class (index 1) should have 8 stars
        self.assertIn("1: ********", result)
    
    def test_bar_graph_average_30(self):
        """Test that class with average 30 shows 3 stars"""
        result = bar_graph()
        self.assertIn("2: ***", result)


class TestPascalsTriangle(unittest.TestCase):
    """Test cases for pascals_triangle function"""
    
    def test_row_zero(self):
        """Test row 0: [1]"""
        result = pascals_triangle(0)
        expected = [1]
        self.assertEqual(result, expected)
    
    def test_row_one(self):
        """Test row 1: [1, 1]"""
        result = pascals_triangle(1)
        expected = [1, 1]
        self.assertEqual(result, expected)
    
    def test_row_two(self):
        """Test row 2: [1, 2, 1]"""
        result = pascals_triangle(2)
        expected = [1, 2, 1]
        self.assertEqual(result, expected)
    
    def test_row_five(self):
        """Test row 5: [1, 5, 10, 10, 5, 1]"""
        result = pascals_triangle(5)
        expected = [1, 5, 10, 10, 5, 1]
        self.assertEqual(result, expected)
    
    def test_row_four(self):
        """Test row 4: [1, 4, 6, 4, 1]"""
        result = pascals_triangle(4)
        expected = [1, 4, 6, 4, 1]
        self.assertEqual(result, expected)
    
    def test_row_six(self):
        """Test row 6: [1, 6, 15, 20, 15, 6, 1]"""
        result = pascals_triangle(6)
        expected = [1, 6, 15, 20, 15, 6, 1]
        self.assertEqual(result, expected)
    
    def test_symmetry(self):
        """Test that Pascal's triangle row is symmetric"""
        result = pascals_triangle(7)
        self.assertEqual(result, result[::-1])
    
    def test_length(self):
        """Test that row n has n+1 elements"""
        for n in range(8):
            result = pascals_triangle(n)
            self.assertEqual(len(result), n + 1)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
