from collections import Counter
import string

def scanTextFile(file_path): 
    """
    Reads the content of a text file and returns it as a string.

    :param file_path: The path to the text file to be read.
    :return: A string containing the contents of the file.
    :raises FileNotFoundError: If the file cannot be found at the given path.
    :raises IOError: If there is an error while reading the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} could not be found.")
    except IOError:
        raise IOError(f"An error occurred while reading the file at {file_path}.")

def get_top_5_words(paragraph):
    """
    This function returns the top 5 most common words from the input.  If a file path is provided, the function reads the content from the file.
    Otherwise, it treats the input as a plain paragraph. The function ignores punctuation, possessive forms (e.g., "word's"),
    and ensures that words containing numbers (e.g., "p53") are kept intact, while pure numbers (e.g., "53") are excluded.

    :param paragraph: A string that can either be:
        1. A paragraph of text, or
        2. A file path to a `.txt` file. If a file path is provided, the function attempts to read the content of the file.
        
    :return: A list of the top 5 most common words in the paragraph or file, in the form of a list of tuples.
        Each tuple contains a word (string) and its count (integer) representing the number of times it appears.
        The list is sorted in descending order by word frequency. If there are fewer than 5 distinct words, 
        the list will contain fewer entries.

    :raises FileNotFoundError: If the file at the given path cannot be found.
    :raises IOError: If there is an error while reading the file.
    """
    file_content = ""
    try:
        file_content = scanTextFile(paragraph)
    except:
        file_content = paragraph

    # Define a translation table that maps puncutation to an empty string 
    table = str.maketrans("", "", string.punctuation)
    
    # Remove possessive grammar, spaces, and any numbers (e.g. keeps word = p53 but not word = 53)
    words = file_content.lower().replace("'s", "")
    words = words.split()
    cleaned_words = [word.translate(table) for word in words if word.translate(table).isalnum() and any(char.isalpha() for char in word)]

    # Count the frequency of each word using Counter
    word_count = Counter(cleaned_words)

    top_5 = word_count.most_common(5)

    return top_5

