def create_matrix():
    matrix = []
    for i in range(4):
        row = input("Enter a row of 4 letters: ")
        if len(row) != 4 or not all(letter.isalpha() and len(letter) == 1 for letter in row):
            print("Invalid input. Please enter 4 letters.")
            return create_matrix()
        matrix.append(list(row))
    return matrix
