import datetime
n = int(input('savollar soni: '))
x = datetime.datetime.now()
print(f'test boshlanish vaqti {x}')
a = datetime.timedelta(minutes=n*1.5)
print(f'test tugashi vaqti {a+x}')
