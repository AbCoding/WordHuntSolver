# Step 1: Read the Input Text File
with open('Words.txt', 'r') as file:
    content = file.read().split()

# Step 2: Filter Words of Desired Length n
n = 5  # Change this to the desired word length

def GenerateTextFile(n):
    filtered_words = [word for word in content if len(word) == n]

    # Step 3: Write Filtered Words to Output Text File
    with open(f'output_{n}.txt', 'w') as file:
        for word in filtered_words:
            file.write(word + '\n')

for i in range(3,20):
    GenerateTextFile(i)
print(f"Filtered words of length {n} have been saved in 'output_{n}.txt' file.")
