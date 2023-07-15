
from nltk.corpus import words
from nltk.corpus import wordnet
import random
import string
filename = 'words.txt'
def generateRrandomWord(length):
    while True:
        word_list = words.words()
        random_word = random.choice(word_list)
        synsets = wordnet.synsets(random_word)
        is_noun = any(synset.pos() == 'n' for synset in synsets)
        if is_noun and (len(random_word) == length):
            return random_word

def fileWriter(word):
    word += " "
    with open(filename, 'a') as fl:
       fl.write(word.capitalize())
def passwordGenerator(filename):
    length = int(input('Введите желаемую длину пароля (от 8 до 10 символов) - '))
    while (length < 8) or (length > 10):
        print("Ошибка ввода! Введите число от 8 до 10")
        length = int(input())
    with open(filename, 'r') as fl:
        content = fl.read()
        list_words = content.split()
        paara = random.choice(list_words), random.choice(list_words)
        while len(str(paara[0] + paara[1])) != length:
            paara = random.choice(list_words), random.choice(list_words)
        password = str(paara[0] + paara[1])
        print(f'Сгенерированный пароль = {password}')
        return
def main():
    while True:
        print("1 - Сгенерировать и записать слово в файл;")
        print("2 - Сгенерировать ключ;")
        print("3 - Выход.")
        data_input = input("Ответ - ")
        print()
        if data_input == '1':
            print('Processing...')
            length = random.randint(3, 7)
            random_word = generateRrandomWord(length)
            print(f'Добавлено новое слово "{random_word.capitalize()}" в файл')
            fileWriter(random_word)
        elif data_input == '2':
            passwordGenerator(filename)
        elif data_input == '3':
            print('- - Exit - -')
            return
        else:
            print('- - Incorrect input value - -')


if __name__ == '__main__':
    main()


