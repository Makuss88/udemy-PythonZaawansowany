import os

def counterWord(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        word_count = len(content.split())
    return word_count


path = r'txt04'
if os.path.isfile(path):
    print("How many words?? {}!".format(counterWord(path)))


os.path.isfile(path) and print("How many words number 2?? {}!".format(counterWord(path)))
