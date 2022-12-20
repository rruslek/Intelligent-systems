import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tkinter import *
from PIL import Image, EpsImagePlugin
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.brush_size = 10
        self.color = "black"
        self.canv = Canvas(root, bg="white", width=280, height=280)
        self.canv.pack(side=TOP)
        self.canv.bind("<B1-Motion>", self.draw)
        button1 = Button(root, text='TEST', command=lambda: self.save_as_png('digit'))
        button1.pack(side=BOTTOM)
        button2 = Button(root, text='CLEAR', command=lambda: self.canv.delete("all"))
        button2.pack(side=BOTTOM)

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

    def save_as_png(self, fileName):
        self.canv.postscript(colormode='gray', file=fileName + '.eps')
        self.parent.destroy()
        EpsImagePlugin.gs_windows_binary = r'C:\Program Files\gs\gs10.00.0\bin\gswin64c'
        img = Image.open(fileName + '.eps')
        img = img.resize((28, 28))
        img.save(fileName + '.png', 'png')


choice = 3
while choice != 0:
    choice = int(input('Что делать?\n1 - Создание и обучение модели НС'
                       '\n2 - Проверка работы модели НС'
                       '\n0 - Выход\n'))
    if choice == 1:
        (x_train, y_train), (x_test, y_test) = mnist.load_data()

        x_train = x_train / 255
        x_test = x_test / 255

        y_train_cat = keras.utils.to_categorical(y_train, 10)
        y_test_cat = keras.utils.to_categorical(y_test, 10)

        x_train = np.expand_dims(x_train, axis=3)
        x_test = np.expand_dims(x_test, axis=3)

        print(x_train.shape)

        model = keras.Sequential([
            Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(28, 28, 1)),
            MaxPooling2D((2, 2), strides=2),
            Conv2D(64, (3, 3), padding='same', activation='relu'),
            MaxPooling2D((2, 2), strides=2),
            Flatten(),
            Dense(128, activation='relu'),
            Dropout(0.15),
            Dense(10, activation='softmax')
        ])

        print(model.summary())

        model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

        his = model.fit(x_train, y_train_cat, batch_size=32, epochs=10, validation_split=0.2)

        scores = model.evaluate(x_test, y_test_cat)
        print("Accuracy: %.2f%%" % (scores[1] * 100))
        model.save('digit_recognition')
        print('\nОбучение завершено. Модель успешно сохранена!')

    if choice == 2:
        model = keras.models.load_model('digit_recognition')
        #print(model.summary())
        print("Модель НС загружена...")
        root = Tk()
        root.geometry("280x330")
        app = Paint(root)
        print("Нарисуйте, пожалуйста, вашу цифру в открывшемся окне")
        root.mainloop()

        image = keras.utils.load_img('digit.png')
        image = image.convert("L")
        input_arr = keras.utils.img_to_array(image)
        input_arr = np.array([input_arr])
        prediction = model.predict(input_arr)
        print("Нарисованной цифрой было: " + str(np.argmax(prediction)))
        #print(prediction)
