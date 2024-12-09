# Project: Reverse a Linked List and Word Frequency Analysis

This project provides the implementation and testing for two problems:

### Problem 1: Reverse a Linked List
- **File**: `linked_list.py`
- **Description**: Given a linked list with integer values, reverse the linked list and print out the reversed result.

### Problem 2: Most Common Words
- **File**: `most_common_words.py`
- **Description**: Given a paragraph of any size, find the top 5 most common words in the paragraph and print the passage along with the list of top 5 words.

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

## Setup Instructions

1. Ensure that **Python 3.x** is installed on your system. No additional dependencies are required unless specified in your `requirements.txt` file.

## Usage Instructions

To find the top 5 most common words in a paragraph, you can use the `get_top_5_words()` function.

### Example:

```python
from most_common_words import get_top_5_words

paragraph = "Python is an interpreted high-level programming language..."
top_5_words = get_top_5_words(paragraph)
print(top_5_words)
