"""
Unit Tests for L1: Array-Hashing Problems
Tests all solutions for each problem
"""

import unittest
import sys
import os
import importlib.util

# Add parent directory to path to import review solutions
review_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, review_dir)

# Import review file dynamically (since filename has date)
review_file = os.path.join(review_dir, '2026-02-27-leetcodes-review.py')
spec = importlib.util.spec_from_file_location("review_solutions", review_file)
review_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(review_module)

# Import solution classes
Solution1_1 = review_module.Solution1_1
Solution1_2 = review_module.Solution1_2
Solution1_3 = review_module.Solution1_3
Solution1_4 = review_module.Solution1_4
Solution1_5 = review_module.Solution1_5
Solution1_6 = review_module.Solution1_6
Solution1_7 = review_module.Solution1_7
Solution1_8 = review_module.Solution1_8
Solution1_9 = review_module.Solution1_9


# ============================================================================
# 1.1 Contains Duplicate Tests
# ============================================================================
class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution1_1()
    
    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        self.assertFalse(self.solution.hasDuplicate(nums))
        self.assertFalse(self.solution.hasDuplicate2(nums))
        self.assertFalse(self.solution.hasDuplicate3(nums))
    
    def test_with_duplicates(self):
        nums = [1, 2, 3, 3]
        self.assertTrue(self.solution.hasDuplicate(nums))
        self.assertTrue(self.solution.hasDuplicate2(nums))
        self.assertTrue(self.solution.hasDuplicate3(nums))
    
    def test_empty_list(self):
        nums = []
        self.assertFalse(self.solution.hasDuplicate(nums))
        self.assertFalse(self.solution.hasDuplicate2(nums))
        self.assertFalse(self.solution.hasDuplicate3(nums))
    
    def test_single_element(self):
        nums = [42]
        self.assertFalse(self.solution.hasDuplicate(nums))
        self.assertFalse(self.solution.hasDuplicate2(nums))
        self.assertFalse(self.solution.hasDuplicate3(nums))
    
    def test_all_identical(self):
        nums = [7, 7, 7, 7]
        self.assertTrue(self.solution.hasDuplicate(nums))
        self.assertTrue(self.solution.hasDuplicate2(nums))
        self.assertTrue(self.solution.hasDuplicate3(nums))


# ============================================================================
# 1.2 Valid Anagram Tests
# ============================================================================
class TestValidAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution1_2()
    
    def test_valid_anagram(self):
        s, t = "racecar", "carrace"
        self.assertTrue(self.solution.isAnagram(s, t))
        self.assertTrue(self.solution.isAnagram2(s, t))
        self.assertTrue(self.solution.isAnagram3(s, t))
    
    def test_not_anagram(self):
        s, t = "jar", "jam"
        self.assertFalse(self.solution.isAnagram(s, t))
        self.assertFalse(self.solution.isAnagram2(s, t))
        self.assertFalse(self.solution.isAnagram3(s, t))
    
    def test_different_lengths(self):
        s, t = "abc", "ab"
        self.assertFalse(self.solution.isAnagram(s, t))
        self.assertFalse(self.solution.isAnagram2(s, t))
        self.assertFalse(self.solution.isAnagram3(s, t))
    
    def test_empty_strings(self):
        s, t = "", ""
        self.assertTrue(self.solution.isAnagram(s, t))
        self.assertTrue(self.solution.isAnagram2(s, t))
        self.assertTrue(self.solution.isAnagram3(s, t))
    
    def test_same_characters_different_counts(self):
        s, t = "aabb", "ab"
        self.assertFalse(self.solution.isAnagram(s, t))
        self.assertFalse(self.solution.isAnagram2(s, t))
        self.assertFalse(self.solution.isAnagram3(s, t))


# ============================================================================
# 1.3 Two Sum Tests
# ============================================================================
class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution1_3()
    
    def test_basic_example_1(self):
        nums, target = [3, 4, 5, 6], 7
        result1 = self.solution.twoSum(nums, target)
        result2 = self.solution.twoSum2(nums, target)
        result3 = self.solution.twoSum3(nums, target)
        self.assertEqual(sorted(result1), [0, 1])
        self.assertEqual(sorted(result2), [0, 1])
        self.assertEqual(sorted(result3), [0, 1])
    
    def test_basic_example_2(self):
        nums, target = [4, 5, 6], 10
        result1 = self.solution.twoSum(nums, target)
        result2 = self.solution.twoSum2(nums, target)
        result3 = self.solution.twoSum3(nums, target)
        self.assertEqual(sorted(result1), [0, 2])
        self.assertEqual(sorted(result2), [0, 2])
        self.assertEqual(sorted(result3), [0, 2])
    
    def test_negative_numbers(self):
        nums, target = [-1, -2, -3, -4, -5], -8
        result1 = self.solution.twoSum(nums, target)
        result2 = self.solution.twoSum2(nums, target)
        result3 = self.solution.twoSum3(nums, target)
        self.assertEqual(sorted(result1), [2, 4])
        self.assertEqual(sorted(result2), [2, 4])
        self.assertEqual(sorted(result3), [2, 4])
    
    def test_duplicate_values(self):
        nums, target = [3, 3], 6
        result1 = self.solution.twoSum(nums, target)
        result2 = self.solution.twoSum2(nums, target)
        result3 = self.solution.twoSum3(nums, target)
        self.assertEqual(sorted(result1), [0, 1])
        self.assertEqual(sorted(result2), [0, 1])
        self.assertEqual(sorted(result3), [0, 1])


# ============================================================================
# 1.4 Group Anagrams Tests
# ============================================================================
class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution1_4()
    
    def test_basic_example_1(self):
        strs = ["act", "pots", "tops", "cat", "stop", "hat"]
        result1 = self.solution.groupAnagrams(strs)
        result2 = self.solution.groupAnagrams2(strs)
        
        # Sort each group and the result for comparison
        result1 = [sorted(group) for group in result1]
        result1.sort()
        result2 = [sorted(group) for group in result2]
        result2.sort()
        
        expected = [sorted(["hat"]), sorted(["act", "cat"]), sorted(["stop", "pots", "tops"])]
        expected.sort()
        
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
    
    def test_basic_example_2(self):
        strs = ["x"]
        result1 = self.solution.groupAnagrams(strs)
        result2 = self.solution.groupAnagrams2(strs)
        self.assertEqual(result1, [["x"]])
        self.assertEqual(result2, [["x"]])
    
    def test_empty_string(self):
        strs = [""]
        result1 = self.solution.groupAnagrams(strs)
        result2 = self.solution.groupAnagrams2(strs)
        self.assertEqual(result1, [[""]])
        self.assertEqual(result2, [[""]])
    
    def test_no_anagrams(self):
        strs = ["abc", "def", "ghi"]
        result1 = self.solution.groupAnagrams(strs)
        result2 = self.solution.groupAnagrams2(strs)
        
        result1 = [sorted(group) for group in result1]
        result1.sort()
        result2 = [sorted(group) for group in result2]
        result2.sort()
        
        expected = [sorted(["abc"]), sorted(["def"]), sorted(["ghi"])]
        expected.sort()
        
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)


# ============================================================================
# 1.5 Top K Frequent Elements Tests
# ============================================================================
class TestTopKFrequent(unittest.TestCase):
    def setUp(self):
        self.solution = Solution1_5()
    
    def test_basic_example_1(self):
        nums, k = [1, 2, 2, 3, 3, 3], 2
        result1 = sorted(self.solution.topKFrequent(nums, k))
        result2 = sorted(self.solution.topKFrequent2(nums, k))
        result3 = sorted(self.solution.topKFrequent3(nums, k))
        expected = [2, 3]
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)
    
    def test_basic_example_2(self):
        nums, k = [7, 7], 1
        result1 = self.solution.topKFrequent(nums, k)
        result2 = self.solution.topKFrequent2(nums, k)
        result3 = self.solution.topKFrequent3(nums, k)
        self.assertEqual(result1, [7])
        self.assertEqual(result2, [7])
        self.assertEqual(result3, [7])
    
    def test_single_element(self):
        nums, k = [1], 1
        result1 = self.solution.topKFrequent(nums, k)
        result2 = self.solution.topKFrequent2(nums, k)
        result3 = self.solution.topKFrequent3(nums, k)
        self.assertEqual(result1, [1])
        self.assertEqual(result2, [1])
        self.assertEqual(result3, [1])
    
    def test_mixed_frequencies(self):
        nums, k = [1, 1, 1, 2, 2, 3], 2
        result1 = sorted(self.solution.topKFrequent(nums, k))
        result2 = sorted(self.solution.topKFrequent2(nums, k))
        result3 = sorted(self.solution.topKFrequent3(nums, k))
        expected = [1, 2]
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)


# ============================================================================
# 1.6 Encode and Decode Strings Tests
# ============================================================================
class TestEncodeDecode(unittest.TestCase):
    def setUp(self):
        self.solution = Solution1_6()
    
    def test_basic_example(self):
        strs = ["neet", "code", "love", "you"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)
    
    def test_empty_strings(self):
        strs = ["", "hello", ""]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)
    
    def test_single_string(self):
        strs = ["test"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)
    
    def test_special_characters(self):
        strs = ["hello#world", "test#123"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs)


# ============================================================================
# 1.7 Product of Array Except Self Tests
# ============================================================================
class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution1_7()
    
    def test_basic_example_1(self):
        nums = [1, 2, 4, 6]
        result1 = self.solution.productExceptSelf(nums)
        result2 = self.solution.productExceptSelf2(nums)
        expected = [48, 24, 12, 8]
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
    
    def test_basic_example_2(self):
        nums = [-1, 0, 1, 2, 3]
        result1 = self.solution.productExceptSelf(nums)
        result2 = self.solution.productExceptSelf2(nums)
        expected = [0, -6, 0, 0, 0]
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
    
    def test_two_elements(self):
        nums = [2, 3]
        result1 = self.solution.productExceptSelf(nums)
        result2 = self.solution.productExceptSelf2(nums)
        expected = [3, 2]
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
    
    def test_with_zeros(self):
        nums = [0, 1, 2]
        result1 = self.solution.productExceptSelf(nums)
        result2 = self.solution.productExceptSelf2(nums)
        expected = [2, 0, 0]
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)


# ============================================================================
# 1.8 Valid Sudoku Tests
# ============================================================================
class TestValidSudoku(unittest.TestCase):
    def setUp(self):
        self.solution = Solution1_8()
    
    def test_valid_board(self):
        board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertTrue(self.solution.isValidSudoku(board))
    
    def test_invalid_row(self):
        board = [
            ["5","3","3",".","7",".",".",".","."],  # Duplicate 3 in row
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertFalse(self.solution.isValidSudoku(board))
    
    def test_invalid_column(self):
        board = [
            ["5","3",".",".","7",".",".",".","."],
            ["5",".",".","1","9","5",".",".","."],  # Duplicate 5 in column
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertFalse(self.solution.isValidSudoku(board))


# ============================================================================
# 1.9 Longest Consecutive Sequence Tests
# ============================================================================
class TestLongestConsecutive(unittest.TestCase):
    def setUp(self):
        self.solution = Solution1_9()
    
    def test_basic_example_1(self):
        nums = [2, 20, 4, 10, 3, 4, 5]
        result1 = self.solution.longestConsecutive(nums)
        result2 = self.solution.longestConsecutive2(nums)
        self.assertEqual(result1, 4)  # [2,3,4,5]
        self.assertEqual(result2, 4)
    
    def test_basic_example_2(self):
        nums = [0, 3, 2, 5, 4, 6, 1, 1]
        result1 = self.solution.longestConsecutive(nums)
        result2 = self.solution.longestConsecutive2(nums)
        self.assertEqual(result1, 7)  # [0,1,2,3,4,5,6]
        self.assertEqual(result2, 7)
    
    def test_empty_array(self):
        nums = []
        result1 = self.solution.longestConsecutive(nums)
        result2 = self.solution.longestConsecutive2(nums)
        self.assertEqual(result1, 0)
        self.assertEqual(result2, 0)
    
    def test_single_element(self):
        nums = [100]
        result1 = self.solution.longestConsecutive(nums)
        result2 = self.solution.longestConsecutive2(nums)
        self.assertEqual(result1, 1)
        self.assertEqual(result2, 1)
    
    def test_no_consecutive(self):
        nums = [1, 3, 5, 7]
        result1 = self.solution.longestConsecutive(nums)
        result2 = self.solution.longestConsecutive2(nums)
        self.assertEqual(result1, 1)
        self.assertEqual(result2, 1)


# ============================================================================
# Test Runner
# ============================================================================
def run_all_tests():
    """Run all unit tests for L1 problems"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestContainsDuplicate))
    suite.addTests(loader.loadTestsFromTestCase(TestValidAnagram))
    suite.addTests(loader.loadTestsFromTestCase(TestTwoSum))
    suite.addTests(loader.loadTestsFromTestCase(TestGroupAnagrams))
    suite.addTests(loader.loadTestsFromTestCase(TestTopKFrequent))
    suite.addTests(loader.loadTestsFromTestCase(TestEncodeDecode))
    suite.addTests(loader.loadTestsFromTestCase(TestProductExceptSelf))
    suite.addTests(loader.loadTestsFromTestCase(TestValidSudoku))
    suite.addTests(loader.loadTestsFromTestCase(TestLongestConsecutive))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success: {result.testsRun - len(result.failures) - len(result.errors)}")
    print("="*70)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    run_all_tests()
