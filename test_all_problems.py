import unittest
import time
from most_common_words import get_top_5_words 
from linked_list import LinkedList
import os

# Base test class with common setup and teardown logic
class BaseTest(unittest.TestCase):
    def setUp(self):
        # Record start time, automatically called with unittest
        self.start_time = time.time()

    def tearDown(self):
        # Record end time, automatically called with unittest
        elapsed_time = time.time() - self.start_time
        print(f"{self._testMethodName} took {elapsed_time:.6f} seconds")


def assertCollectionsEqual(actual, expected): 
    """
    Custom assertion to compare two collections of (word, count) pairs without considering order.

    :param actual: The result from the function, e.g., a list of (word, count) tuples.
    :param expected: The expected result, e.g., a list or set of (word, count) tuples.
    :raises AssertionError: If the collections are not equal.
    """
    actual = set(actual)
    expected = set(expected)
    if (actual != expected): 
        raise AssertionError(
            f"Collections do not match:\n"
            f"Actual:   {actual}\n"
            f"Expected: {expected}\n"
            f"Missing:  {expected - actual}\n"
            f"Extra:    {actual - expected}"
        )
    
class TestTopWordsFunction(BaseTest):

    def test_basic_paragraph(self):
        paragraph = """Python is an interpreted high-level programming language for general-purpose programming. 
        Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
        Its language constructs and object-oriented approach aim to help programmers write clear, logical code."""
        # convert to set for comparison where order doesn't matter
        expected_output = {
            ('python', 2),
            ('programming', 2),
            ('language', 2),
            ('code', 2),
            ('its', 2),
        }
        result = set(get_top_5_words(paragraph))
        assertCollectionsEqual(result, expected_output)
    
    def test_single_word_repeated(self):
        paragraph = "hello hello hello hello hello"
        expected_output = [
            ('hello', 5)
        ]
        result = get_top_5_words(paragraph)
        assertCollectionsEqual(result, expected_output)
    
    def test_paragraph_with_punctuation(self):
        paragraph = "Python's philosophy, Python's code, and Python's design!"
        expected_output = [
            ('python', 3),
            ('philosophy', 1),
            ('code', 1),
            ('and', 1),
            ('design', 1)
        ]
        
        result = get_top_5_words(paragraph)
        assertCollectionsEqual(result, expected_output)
    
    def test_case_insensitivity(self):
        paragraph = "Python python PYTHON Python"
        expected_output = [
            ('python', 4)
        ]
        result = get_top_5_words(paragraph)
        assertCollectionsEqual(result, expected_output)
    
    def test_paragraph_with_numbers(self):
        paragraph = "hello 123 hello p53 123 123"
        expected_output = [
            ('hello', 2),
            ('p53', 1)
        ]
        result = get_top_5_words(paragraph)
        assertCollectionsEqual(result, expected_output)
    
    def test_empty_paragraph(self):
        paragraph = ""
        expected_output = []
        result = get_top_5_words(paragraph)
        assertCollectionsEqual(result, expected_output)
    
    # test reading in a file path
    def test_sherlock_text_file(self):
        file_dir = os.path.dirname(__file__) 
        file_path = os.path.join(file_dir, "sherlock.txt") 

        expected_output = [
            ('adventure', 6), ('scandal', 1), ('a', 2), ('of', 7), ('the', 17)
        ]

        result = get_top_5_words(file_path)
        assertCollectionsEqual(result, expected_output)

class TestLinkedList(BaseTest):

    # Test the append function
    def test_append(self):
        linked_list = LinkedList()
        linked_list.append(-10)
        linked_list.append(20)
        linked_list.append(-30)

        current = linked_list.head
        self.assertEqual(current.data, -10)
        current = current.next
        self.assertEqual(current.data, 20)
        current = current.next
        self.assertEqual(current.data, -30)
    
    # Test the reversed function
    def test_reverse(self):
        linked_list = LinkedList()
        linked_list.append(10)
        linked_list.append(20)
        linked_list.append(30)
        
        linked_list.reverse()

        current = linked_list.head
        self.assertEqual(current.data, 30)
        current = current.next
        self.assertEqual(current.data, 20)
        current = current.next
        self.assertEqual(current.data, 10)
    
    # Test append function large numbers
    def test_large_numbers(self):
        linked_list = LinkedList()
        large_number = 10**100  # A very large number
        linked_list.append(large_number)
        linked_list.append(-large_number)

        current = linked_list.head
        self.assertEqual(current.data, large_number)  
        current = current.next
        self.assertEqual(current.data, -large_number) 

    # Testing append zero
    def test_zero(self):
        linked_list = LinkedList()
        linked_list.append(0)

        current = linked_list.head
        self.assertEqual(current.data, 0)  
    
    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            linked_list = LinkedList()
            linked_list.append("string") 
    
if __name__ == "__main__":
    unittest.main()  # Run the test suite