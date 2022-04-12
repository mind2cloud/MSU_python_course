dictionary = {'France': 'Paris', 'Russia': 'Moscow', 'USA': 'Washington DC',
              'China': 'Beijing', 'UK': 'London', 'Hungary': 'Budapest'}
inp = '1'
while inp != 'exit':
    inp = str(input("Введите ключ: "))
    if inp in dictionary:
        print('Есть такой ключ, значение: ', dictionary[inp])
    else:
        yes_no = str(input('Нет такого ключа. Хотите создать? Yes/No: '))
        if yes_no == "Yes":
            item = str(input("Введите новое значение: "))
            dictionary[inp] = item
        else:
            continue

else:
    exit()

#если ключа нет, писать нет такого ключа, если нажал exit, то выход
#H/W Добавить возможность задавать новые ключи, которые не найдены