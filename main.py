# -*- coding: utf-8 -*-
from tkinter import *
from random import *

n = 7
q=randint(0, n)
cnt=0
correct=0

questionblock1=[['На каком этаже находится кафедра аналитической химии СПХФА?',
                'Химический анализ бывает количественным и..',
                'Классический анализ включает такие методы как поляриметрия, гравиметрия, фотоколориметрия, титрометрия, рефрактометрия. Укажите лишнее',
                'Приближенно вычислите: 30.004+94.34506',
                'Приближенно вычислите: 20.4568/30.00',
                'К статистическим метрикам относятся: дисперсия, титр по веществу, детерминант, математическое ожидание. Укажите лишнее',
                'Заполните пропуски. Титрование бывает обратное, ..., по замещению, ...'],
                ['Что такое осень?',
                 '']
                ]
answerblock1=[[u"на четвертом",
              u'качественным',
              u'гравиметрия, титрометрия',
              u'64.349',
              u'0.6819',
              u'титр по веществу, детерминант',
              u'прямое, инверсное'],
              [u'это небо']
              ]


root=Tk()

Mainlabel=Label(root, text="Anchem Time")
Mainlabel.pack(side='top')
quest=Label(root, text=questionblock1[cnt][q])
quest.pack()
entry=Entry()
entry.pack()

def out():
    global q, cnt, correct
    ansenter = entry.get()
    ans=ansenter.lower()
    if ans == answerblock1[cnt][q]:
        n = n-1
        q = randint(0, n)
        correct+=1
        entry.delete(0, END)
        quest.config(text=questionblock1[cnt][q])

        if correct == 3:
            cnt += 1
            q = 0
            quest.config(text=questionblock1[cnt][q])

button1=Button(root, text="Ввести ответ", command=out)
button1.pack()

root.mainloop()