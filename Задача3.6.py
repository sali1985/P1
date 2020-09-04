#Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def int_func(*args):
    words = input('Введите любые слова ')
    print(words.title())
    return words
int_func()