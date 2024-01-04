def check_word_in_file(input_letters, file_path):
    # Read words from the text file and store them in a list
    with open(file_path, 'r') as file:
        words = [word.strip().lower() for word in file.readlines()]

    # Convert input letters to lowercase for case-insensitive comparison
    input_letters = input_letters.lower()

    # Check if input letters are present in the list of words
    if input_letters in words:
        return True
    else:
        return False


def GenerateListFromFile(file_path):
    with open(file_path, 'r') as file:
        words = [word.strip().lower() for word in file.readlines()]
    return words



