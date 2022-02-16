import datetime
from random import randint, random


Savollar = []
Kalitlar = []
Togri_javoblar = []
Entered_answer = []


while True:
    sorov_main = str(input("SAVOL QOSHISH UCHUN -> 1:\nTEST ISHLASH UCHUN -> 2:\n>>>"))
    if sorov_main == '1':
        while True:
            Savol = str(input("Savol matni:\n>>>"))
            if Savol == '0':
                break
            Savollar.append(Savol)
            A_kalit = str(input("A): "))
            B_kalit = str(input("B): "))
            C_kalit = str(input("C): "))
            text = f'A) {A_kalit}\nB) {B_kalit}\nC) {C_kalit}'
            Kalitlar.append(text)
            javob_kalit = str(input("Qaysi kalit togri\n>>>"))
            Togri_javoblar.append(javob_kalit)
            
    elif sorov_main == '2':
        print('START TEST')
        print(f' there are {len(Savollar)} questions in the test')
        
        if len(Savollar)==0:
            print('you haven\'t added any questions yet')
            continue
        
         
        else:
            ball = 0
            Savol_sorash= int(input('Nechta savol ishlamoqchisiz?:'))
            
            x = datetime.datetime.now()
            print(f'test boshlanish vaqti {x}')
            a = datetime.timedelta(minutes=Savol_sorash*1.5)
            print(f'test tugashi vaqti {a+x}')
            for i in range(Savol_sorash):
                b = randint(0, len(Savollar))
                
            #for i in range(len(Savollar)):
                a = f'{i+1} - {Savollar[b]} \n{Kalitlar[b]}'
                print(a)
                kalit = str(input("JAVOB: "))
                Entered_answer.append(kalit)
                if Entered_answer[i]==Togri_javoblar[b]:
                    ball+=1
            print(ball, 'togri')
            z = datetime.datetime.now()
            print(f'tugash vaqtingiz {z}')
            
            
            