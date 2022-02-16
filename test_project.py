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
            for i in range(len(Savollar)):
               a = f'{i+1} - {Savollar[i]} \n{Kalitlar[i]}'
               print(a)
               kalit = str(input("JAVOB: "))
               Entered_answer.append(kalit)
               if Entered_answer[i]==Togri_javoblar[i]:
                 ball+=1
            print(ball, 'togri')