# -*- coding: utf-8 -*-
import random
import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# функции
unique_letters = {}


def manipulate_word(word, skip_prob=0.075, replace_prob=0.05):
    manipulated_word = list(word)

    for i in range(len(manipulated_word)):
        if random.random() < skip_prob:
            manipulated_word[i] = ''
        elif random.random() < replace_prob:
            new_char = chr(random.randint(ord('а'), ord('я')))
            manipulated_word[i] = new_char

    return ''.join(manipulated_word)


def generate_variations(input_strings, num_variations):
    variations = []

    for input_word in input_strings:
        input_n = [input_word, '']

        if input_word.find('улица') != -1:
            input_n[1] = 'улица'
        elif input_word.find('переулок') != -1:
            input_n[1] = 'переулок'
        elif input_word.find('площадь') != -1:
            input_n[1] = 'площадь'
        elif input_word.find('проспект') != -1:
            input_n[1] = 'проспект'

        variations_for_input = []

        for _ in range(num_variations):
            out = manipulate_word(input_n[0])
            # добавляется в массив и "коверкается"
            variations.append(out + manipulate_word(input_n[1]))

    return variations


def generate_array(length, repeats):
    diagonal = np.eye(length)
    repeated_diagonal = np.repeat(diagonal, repeats, axis=0)
    return repeated_diagonal


def tokenize_and_convert_to_numbers(array, lete):
    if (len(lete) == 0):
        unique_letters = {}  # Словарь для хранения уникальных букв и их номеров
    else:
        unique_letters = lete
    result = []  # Результирующий массив
    bigarr = []
    z = len(array)
    r = 0
    while r < z:
        string = array[r].lower()
        result = []
        for letter in string:
            if letter not in unique_letters:
                unique_letters[letter] = len(unique_letters) + 1
            result.append(unique_letters[letter])
        r += 1
        bigarr.append(result)
    return bigarr, unique_letters


# код
inputs = [["Невский проспект", "Большая Морская улица", "Малая Морская улица", "Большой проспект Петроградской стороны",
           "6-я линия Васильевского острова", "Московский проспект", "Литейный проспект", "Гороховая улица",
           "Рубинштейна улица", "Большая Конюшенная улица", "Итальянская улица", "Фонтанка", "Большая Морская улица",
           "Малая Морская улица", "Лиговский проспект", "Вознесенский проспект", "Большой Сампсониевский проспект",
           "Казанская улица", "Пушкинская улица", "4-я Советская улица", "7-я линия Васильевского острова"]]
# репиты
repeats = 100

z = 0

padded_sequences = []
input_sequences = []
max_sequence_length = 0
unique = {}
while (z < repeats):
    if (len(unique) > 0):
        uni = unique
    if (z != 0):
        inputs.append(generate_variations(inputs[0], 1))
    arrnow = inputs[z]
    input_sequenc, uni = tokenize_and_convert_to_numbers(arrnow, unique)
    input_sequences.append(input_sequenc)  # добавление токинизированого инпута
    maxnow = max([len(seq) for seq in input_sequences[z]])
    if (max_sequence_length < maxnow):
        max_sequence_length = maxnow
    z += 1

z = 0
while (z < repeats):
    padded_sequences.append(pad_sequences(input_sequences[z], maxlen=max_sequence_length))
    z += 1

# print (padded_sequences[0])
# print(max_sequence_length)
# model = Sequential()
# model.add(Embedding(input_dim=len(padded_sequences[0][0]), output_dim=len(padded_sequences[0][0]), input_length=max_sequence_length))
# model.add(layers.Dense(2, activation="relu"))
# model.add(Dense(len(inputs[0]), activation='softmax'))

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(len(padded_sequences[0][0]), 1)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(len(inputs[0]), activation='softmax')
])

# Компиляция модели
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Создание целевых значений для обучения
# Пример: создание one-hot векторов для каждого входа
target_values = np.eye(len(inputs[0]))

# Обучение модели
num_epochs = 10
batch_size = 32

# Замените placeholder на ваши данные для обучения
x_train = np.array(padded_sequences)
y_train = target_values

model.fit(x_train, y_train, epochs=num_epochs, batch_size=batch_size)
