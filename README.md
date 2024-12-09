# Project: Reverse a Linked List and Word Frequency Analysis

## Project Structure

- **`most_common_words.py`**: Contains the implementation to return the top 5 most common words from a paragraph.
- **`linked_list.py`**: Contains the implementation of the linked list class, including functions to reverse and append to the list.
- **`test_all_problems.py`**: A test suite that validates the functionality of both the word processing and linked list logic.
- **`sherlock.txt`**: A sample text file used for testing the `most_common_words.py` script.

## Requirements

- **Python 3.x**: The project is written in Python 3.x.
- **unittest**: For running tests and validating the functionality of the code.
- **time**: For calculating the time taken to run a test case.
- **os**: For handling file paths in relation to file names.

## Purpose

This project provides the implementation and testing for two problems:

### Problem 1: Reverse a Linked List
- **File**: `linked_list.py`
- **Description**: Given a linked list with integer values, reverse the linked list and print out the reversed result.

### Problem 2: Most Common Words
- **File**: `most_common_words.py`
- **Description**: Given a paragraph of any size, find the top 5 most common words in the paragraph and print the passage along with the list of top 5 words.

## Usage Instructions
Ensure that **Python 3.x** is installed on your system.

### Problem 1: Reverse a Linked List
`class LinkedList()`

Returns an empty singly linked list with the following attributes:

- **head**  
  The first object in the list. `_None_` if the list is empty.

- **tail**  
  The last object in the list. `_None_` if the list is empty.

The LinkedList class also supports the following methods: 
- **append(integer x)**
  Add integer x to the right side of the list. Returns a `ValueError` if x is not an integer. 

- **print_list**  
  Print out the list from head to tail with `->` denoting connections between elements

- **reverse**  
  Reverses the order of nodes in the linked list, updating the `head` to the last node and the `tail` to the first node.


### Problem 2: Most Common Words

To find the top 5 most common words in a paragraph, you can use the `get_top_5_words()` function.

This function returns the top 5 most common words from the input. If a file path is provided, the function reads the content from the file. Otherwise, it treats the input as a plain paragraph. The function ignores punctuation, possessive forms (e.g., "word's"), and ensures that words containing numbers (e.g., "p53") are kept intact, while pure numbers (e.g., "53") are excluded.

#### Function: `get_top_5_words(paragraph)`

- **Description:**  
  This function returns the top 5 most common words from the input. If a file path is provided, the function reads the content from the file. Otherwise, it treats the input as a plain paragraph. The function ignores punctuation, possessive forms (e.g., "word's"), and ensures that words containing numbers (e.g., "p53") are kept intact, while pure numbers (e.g., "53") are excluded.

- **Parameters:**  
  - `paragraph` (str): A string that can either be:  
    1. A paragraph of text, or  
    2. A file path to a `.txt` file. If a file path is provided, the function attempts to read the content of the file.

- **Returns:**  
  A list of the top 5 most common words in the paragraph or file, in the form of a list of tuples. Each tuple contains a word (string) and its count (integer) representing the number of times it appears. The list is sorted in descending order by word frequency. If there are fewer than 5 distinct words, the list will contain fewer entries.

- **Raises:**  
  - `FileNotFoundError`: If the file at the given path cannot be found.  
  - `IOError`: If there is an error while reading the file.

### Example:

```python
from most_common_words import get_top_5_words

paragraph = "Python is an interpreted high-level programming language..."
top_5_words = get_top_5_words(paragraph)
print(top_5_words)
```

## Testing Instructions
To ensure the correct functionality of your code, use the provided unittest test suite and add to it. This test suite will output the results to the console.

### Run Tests:
To run the tests, ensure you are in the folder `Coding-Assessment` and run `python3 test_all_problems.py`

### Test Coverage:
  #### `linked_list.py` tests: 
  - **Test Append Function:**: Verifies that positive and negative integers are correctly appended to the linked list in the proper order.
  - **Test Reverse Function:**: Tests that the reverse method correctly reverses the order of elements in the linked list. 
  - **Test Large Numbers:**: Ensures the append function can handle very large numbers (e.g., 10^100) and correctly adds both positive and negative versions of this large number.
  - **Test Append Zero:** Confirms that zero (0) can be appended to the linked list, and the list should correctly reflect its presence.

  #### `most_common_word.py` tests: 
  - **Basic Paragraph:** Tests whether the top 5 words are correctly extracted from a basic paragraph.
  - **Single Word Repeated:** Tests whether a paragraph with a repeated word returns the correct count for that word.
  - **Paragraph with Punctuation:** Verifies that punctuation is correctly removed from the paragraph.
  - **Case Insensitivity:** Ensures the function treats uppercase and lowercase letters as the same.
  - **Paragraph with Numbers:** Validates that numbers (like p53) are kept intact, but pure numbers (like 53) are excluded.
  - **Empty Paragraph:** Ensures the function handles an empty paragraph properly.
  - **Reading in text file:** Ensures function can read from an external text file given path

## Troubleshooting

### Error: File not found
If you're encountering a "file not found" error while testing, ensure that the file exists. If necessary, use absolute paths or adjust the file lookup to point to the correct location.

### Error: ValueError when appending
If you attempt to append an item that is not a valid data type (e.g., trying to append a string to a linked list), a `ValueError` will be raised. Ensure that only valid data types (such as integers or floats) are appended to the list.






