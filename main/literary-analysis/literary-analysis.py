import string
from collections import Counter

# method use to process the text file and read the all text file data
# after read the file remove the punctuation
def process_txt_file(file_path):
    if isinstance(file_path, str) and file_path.endswith('.txt'):
        # Read the file for txt
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        # send the read text for report generate
        generate_report(text.translate(str.maketrans('', '', string.punctuation)))
    else:
        print('File type not supported')

# method use to count each word and generate and print a report
def generate_report(text):
    # Split the text into words
    words = text.split()
    # Count occurrences of each word
    word_count = Counter(words)
    sorted_words = sorted(word_count.items())
    print('# # # # # # # # # # # # # # # # # # # # #')
    print('#           Print Process               #')
    print('# # # # # # # # # # # # # # # # # # # # #')
    print(f"# {'Word':<32}{'Count'} #")
    print("# " * 21)
    # Sort the word count dictionary alphabetically by word
    for word, count in sorted_words:
        print(f"# {word:<35}{' ' * 0 if count > 10 else ' ' * 1}{count} #")
    print("# " * 21)


if __name__ == '__main__':
    process_txt_file(r'C:\Users\njamil\Desktop\Nabeel RND\ren-data-gerator\resource\file1.txt')
    print()
    process_txt_file(r'C:\Users\njamil\Desktop\Nabeel RND\ren-data-gerator\resource\file2.txt')