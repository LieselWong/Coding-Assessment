Project: Reverse a Linked List and Word Frequency Analysis 

This project provides testing and implementation for the following two problems: 

Problem 1 / linked_list.py: 
Given a linked-list with integer values, reverse the linked list.
Print out the reversed result

Problem 2 / most_common_words.py: 
Given a paragraph input of any size, find the top 5 most
common words in the paragraph. 
Print passage and list the top 5 words. 

Files:
    most_common_words.py - Contains the implementation of a program that returns the top 5 words 
    linked_list.py - Contains the implementation of a linked list class, and functions to reverse and append to the list class
    test_all_problems.py – A test suite to validate the functionality of the word processing and extraction logic.
    sherlock.txt – A sample text file for testing most_common_words.py

Requirements:
    Python 3.x - coding language 
    unittest – For running tests and validating the code.
    time - For calculating time taken to run a test case
    os - For finding file path given file name

Setup Instructions:
    Install Dependencies: Ensure that Python 3.x is installed. No additional dependencies are required unless specified in your requirements.txt.

Usage Instructions: 
    get_top_5_words() 
    Function: This function can be used to find the top 5 most common words in a paragraph, excluding punctuation and possessive grammar.

    Instructions:
    At the top of the file include: 
    from most_common_words import get_top_5_words 

    Example: 
    paragraph = "Python is an interpreted high-level programming language..."
    top_5_words = get_top_5_words(paragraph)
    print(top_5_words)


Testing Instructions:
To ensure the correct functionality of your code, use the provided unittest test suite.

    Run Tests:
        The test suite is located in the test_all_problems.py file. 
        To run the tests, ensure you are in the folder 'LieselWong-CodingAssessment' and run python3 test_all_problems.py

    This will execute all the test cases defined and output the results to the console.

    Test Coverage:
        linked_list.py tests: 
        Test Append Function: Verifies that elements are correctly appended to the linked list in the proper order. This test ensures that after appending -10, 20, and -30, the linked list maintains the correct order.

        Test Reverse Function: Tests that the reverse method correctly reverses the order of elements in the linked list. After appending 10, 20, and 30, the list should reverse to 30, 20, 10.

        Test Large Numbers: Ensures the append function can handle very large numbers (e.g., 10^100) and correctly adds both positive and negative versions of this large number.

        Test Append Zero: Confirms that zero (0) can be appended to the linked list, and the list should correctly reflect its presence.

        Test Invalid Data: Verifies that the linked list raises a ValueError if an attempt is made to append invalid data types, such as a string.

        most_common_word.py tests: 
        Basic Paragraph: Tests whether the top 5 words are correctly extracted from a basic paragraph.

        Single Word Repeated: Tests whether a paragraph with a repeated word returns the correct count for that word.

        Paragraph with Punctuation: Verifies that punctuation is correctly removed from the paragraph.

        Case Insensitivity: Ensures the function treats uppercase and lowercase letters as the same.

        Paragraph with Numbers: Validates that numbers (like p53) are kept intact, but pure numbers (like 53) are excluded.

        Empty Paragraph: Ensures the function handles an empty paragraph properly.

        Reading in text file: Ensures function can read from an external text file given path
    
Troubleshooting:

    Error: File not found: If you're encountering a "file not found" error while testing with lab_samples.txt, make sure the file is placed in the correct directory relative to the script. If necessary, use absolute paths or adjust the file lookup to point to the correct location.