#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QRadioButton,QGroupBox, QButtonGroup
from random import shuffle, randint
#Сщздаем обект приложения

class Question():
    def __init__(self, question, right_answer, wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()#окно приложения
main_win.setWindowTitle('Memory Card»')
main_win.resize(600,300)
btn_ok = QPushButton('Ответить')
ab_qvehn = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()#гаризонтальная линия
layout_ans2 = QVBoxLayout()#2 вертикальных будут внутри горизонтал
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)#2 ответа помещаем в первый толбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)#два ответа во 2 столбец
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)#размещаем столбци в отной строке
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)#готовая понель с вариантами ответов
AnsGrupBox = QGroupBox('Результаты теста:')
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Правильный ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft|Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGrupBox.setLayout(layout_res)
layout_Line1 = QHBoxLayout()#линия для вопроса
layout_Line2 = QHBoxLayout()#линия для ответов
layout_Line3 = QHBoxLayout()#для кнопки ответить

layout_Line1.addWidget(ab_qvehn, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))#распологам вопрос по центру линии

layout_Line2.addWidget(RadioGroupBox)#заспологаем группу ответов по линии
layout_Line2.addWidget(AnsGrupBox)
AnsGrupBox.hide()


layout_Line3.addStretch(1)#делаем отступ между кнопкой и вариантом ответов
layout_Line3.addWidget(btn_ok, stretch=2)
layout_Line3.addStretch(1)

layout_card = QVBoxLayout()#создаем главный вертикальный лиаут
layout_card.addLayout(layout_Line1, stretch=2)#добавляем вопрос и делаем растояние между ними
layout_card.addLayout(layout_Line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_Line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)#пробелы между содержимым

def show_result():
    RadioGroupBox.hide()
    AnsGrupBox.show()
    btn_ok.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGrupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)#Сняли ограничения , чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    ab_qvehn.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.skore += 1
        print('Статистика\nВсего вопросов', main_win.total,'\nправильных ответов',main_win.skore )
        print('Рейтинг:',(main_win.skore/main_win.total * 100))
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неправильно!")

question_List = []
question_List.append( Question("Государственный язык Бразилии", 'Португальский', 'Бразильский', 'Испанский' , "Итальянский"))
question_List.append( Question('Какого цвета нет нафлаге России', 'Зеленый', 'Белый', 'Синий' , "Красный"))

def next_question():
    main_win.total += 1
    print('Статистика\nВсего вопросов', main_win.total,'\nправильных ответов',main_win.skore )
    cur_question = randint(0, len(question_List)-1)
    q = question_List[cur_question]
    ask(q)

def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()

main_win.total = 0
main_win.skore = 0


main_win.setLayout(layout_card)
btn_ok.clicked.connect(click_OK)
next_question()
main_win.show()
app.exec()

