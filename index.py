import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Массив входных данных
input_data = ["Невский проспект", "Большая Морская улица", "Малая Морская улица",
              "Большой проспект Петроградской стороны", "6-я линия Васильевского острова", "Московский проспект",
              "Литейный проспект", "Гороховая улица", "Рубинштейна улица", "Большая Конюшенная улица",
              "Итальянская улица", "Фонтанка реки набережная", "Большая Морская улица", "Малая Морская улица",
              "Лиговский проспект", "Вознесенский проспект", "Большой Сампсониевский проспект", "Казанская улица",
              "Пушкинская улица", "4-я Советская улица", "7-я линия Васильевского острова"]

# Создание токенизатора
tokenizer = Tokenizer()
tokenizer.fit_on_texts(input_data)

# Преобразование входных данных в числовые последовательности
input_sequences = tokenizer.texts_to_sequences(input_data)

# Заполнение последовательностей нулями до одинаковой длины
max_sequence_length = max([len(seq) for seq in input_sequences])
padded_sequences = pad_sequences(input_sequences, maxlen=max_sequence_length)

# Создание нейросети
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=400, input_length=max_sequence_length))
model.add(LSTM(400))
model.add(Dense(len(input_data), activation='softmax'))

# Компиляция модели
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Создание массива меток
labels = np.eye(len(input_data))

# Обучение модели
model.fit(padded_sequences, labels, epochs=3000)

# Ввод и предсказание
while True:
    input_word = input("Введите слово: ")
    input_sequence = tokenizer.texts_to_sequences([input_word])
    padded_sequence = pad_sequences(input_sequence, maxlen=max_sequence_length)
    prediction = model.predict(padded_sequence)
    predicted_label = input_data[np.argmax(prediction)]
    print(f"Предсказание: {predicted_label}")
