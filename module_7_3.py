import re


class WordsFinder:
    def __init__(self, *names):
        self.file_names = list(names)

    def get_all_words(self):
        all_words = {}
        unwanted_chars = ",.=!?;:"
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                for char in unwanted_chars:
                    content = content.replace(char, '')
                content = re.sub(r'(?<=\S) - (?=\S)', ' ', content)
                words = content.split()
                all_words[i] = words
        return all_words

    def find(self, word):
        vocab_find = {}
        word = word.lower()
        all_words = self.get_all_words()
        for filename, words in all_words.items():
            if word in words:
                position = words.index(word)
                vocab_find[filename] = position
        return vocab_find

    def count(self, word):
        vocab_count = {}
        word = word.lower()
        all_words = self.get_all_words()
        for filename, words in all_words.items():
            if word in words:
                number = words.count(word)
                vocab_count[filename] = number
        return vocab_count


subject = WordsFinder('test_file.txt')
print(subject.get_all_words())
print(subject.find('teXT'))
print(subject.count('TeXt'))
