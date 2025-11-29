import random
import time
import sys
class id:
    """Индентификационная система"""

    def __init__(self):
        self.login = ""
        self.password = ""
        self.ids = {}

    def Call_Back(self, objekt):
        if objekt == "login":
            return self.login
        elif objekt == "password":
            return self.password
        else:
            return "ERROR"

    def registration(self):
        self.login = input("Придумай логин >>> ")
        self.password = input ( "Придумай пароль >>>")
        self.ids.update({self.login: self.password})

    def get_password(self, login):
        return self.ids[login]


class Bank:
    '''Оплата посредством Stasya Pay'''

    def __init__(self, user_id=None):
        self.card_number = ""
        self.card_date = ""
        self.cvc = ""
        self.id = user_id  # Сохраняем переданный экземпляр id
        self.name = user_id.Call_Back(
            objekt="login") if user_id else "Гость"  # Получаем логин через метод экземпляра
        self.tranzaktion = False
        self.balance = 0

    def Pay(self, summa):
        self.card_number = input("Введи номер карты >>> ")
        self.card_date = input("Срок карты >>> ")
        self.cvc = input("Введи CVC >>> ")

        if self.card_number and self.card_number[0] == '7':
            print (f"{self.name}, подтвердите покупку:\n"
                    f"    Карта Стася банка: {self.card_number}\n"
                    f"    Дата карты: {self.card_date}\n"
                    f"    CVC карты: {self.cvc}\n"
                    f"    Сумма покупки: {summa}\n"
                    f"Для подтверждения покупки наберите yes")
            if input ("Подтвердите покупку >>> ") == "yes":
                if self.balance >= summa:
                    self.balance -= summa
                    print( "Успешная покупка!" )
                    self.tranzaktion = True
                    return self.tranzaktion
                else:
                    print("Недостаточно средств!")
                    self.tranzaktion = False
                    return self.tranzaktion
            else:
                print("Покупка отменена!")
                self.tranzaktion = False
                return self.tranzaktion
        else:
            print(f"Подтвердите покупку:\n"
                    f"    Карта: {self.card_number}\n"
                    f"    Дата карты: {self.card_date}\n"
                    f"    CVC карты: {self.cvc}\n"
                    f"    Сумма покупки: {summa}\n"
                    f"Для подтверждения покупки наберите yes")
            if input("Подтвердите покупку >>> ") == "yes":
                if self.balance >= summa:
                    self.balance -= summa
                    print("Успешная покупка!")
                    self.tranzaktion = True
                    return self.tranzaktion
                else:
                    print("Недостаточно средств!")
                    self.tranzaktion = False
                    return self.tranzaktion
            else:
                print("Покупка отменена!")
                self.tranzaktion = False
                return self.tranzaktion

    def add_balance(self, balance):
        self.balance += balance
        return "Done"

    def remove_balance(self, balance):
        self.balance -= balance
        return "Done"

class notes:
    def __init__(self):
        self.kov = 0
        self.notes = {}
    
    def add_note(self):
        self.kov += 1
        name = input("Введи имя заметки >>> ")
        value = input("Введи текст заметки >>> ")
        self.notes[name] = value

        print("Заметка добавлена")
    
    def remove_note(self):
        name = input("Введи имя заметки >>> ")
        if name in self.notes:
            self.notes.pop(name)
            print(f"Заметка {name} удалена")
        else:
            print(f"Такая заметка ({name}) не найдена")

    def list_notes(self):
        if self.notes:
            for name, note in self.notes.items():
                print(f"У вас {self.kov} заметок")
                print("-"*100)
                print(f"Заметка: {name}\nСодержимое: {note}")
                print("-"*100)
        else:
            print("У вас нет заметок")
    
    def menu(self):

        choice = input("Выбери\n" \
        "1. Добавить заметку\n" \
        "2. Удалить заметку\n" \
        "3. Посмотреть список заметок\n" \
        "4. Выйти\n" \
        "\nВаш выбор >>> ")
            
        if choice == "1":
            self.add_note()
        elif choice == "2":
            self.remove_note()
        elif choice == "3":
            self.list_notes()
        elif choice == "4":
            print("Выход из меню заметок")
            exit
        else:
            print("Вы ввели что-то не то")


class Microscop:
    '''Класс для действий о микроскопе'''
    def __init__(self):
        self.okular = 0
        self.obektiv = 0
    def Count(self, printmode = False):
        '''Функция считает, во сколько раз увеличевает микроскоп. Сбор инфрмации автоматический. Printmode = Fase указывает, нужно ли вернуть (retern) результат или Printmode = True - вернуть и вывести в консоль'''
        self.obektiv = int(input("Введите уведичение обЪектива >>> "))
        self.okular = int(input("Введите уведичение микроскопа >>> "))
        microskop = self.obektiv * self.okular
        if printmode == True:
            print(f"Микроскоп увеличевает в {microskop} раз")
            return microskop
        else:
            return microskop


class math:
    # Математика
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.S = 0.0
        self.P = 0.0
        self.val_to_count_summa = 0
        self.val_to_translate_to_rim = 0
    
    def count_S(self):
        self.a = float(input("Введи длинну прямоугольника >>> "))
        self.b = float(input("Введи ширину прямоугольника >>> "))
        self.S = self.a * self.b
        print(f"Площадь прямоугольника: {self.S}")

    def count_p(self):
        self.a = float(input("Введи длинну прямоугольника >>> "))
        self.b = float(input("Введи ширину прямоугольника >>> "))
        self.P = self.a + self.b
        print(f"Периметр прямоугольника: {self.S}")
    

    def count_summa(self):
        self.val_to_count_summa = input("Введи число >>> ")

        total = 0

        for digit in self.val_to_count_summa:
            total += int(digit)

        print(f"Сумма цифр числа {self.val_to_count_summa}: {total}")


    def to_rimsk(self):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        num = int(input("Введи число >>> "))
        result = ""
        for i in range(len(values)):
            while num >= values[i]:
                result += numerals[i]
                num -= values[i]
        print(f"В римских цифрах: {result}")
        return result

class visokosni_god:
    '''Считаем високосный ли год'''
    def __init__(self):
        self.god = int(input("Введи год: "))
    def count(self):
        if self.god % 4 == 0:
            if self.god % 100 == 0:
                print(f"Год {self.god} - невисоковсный")
                return "Not"
            else:
                print(f"Год {self.god} - високовсный")
                return "Yes"
        else:
            print(f"Год {self.god} - невисоковсный")
            return "Not"


class Vklad:
    def __init__(self):
        self.persent = float(input("Введи процент >>> "))
        self.monny = float(input("Введи сколько денег на начало  >>> "))
        self.srok = int(input("Введи на сколько лет >>> "))
    def count(self):
        for year in range(self.srok):
            self.monny += (self.monny/100) * self.persent
        doxod = round(self.monny, 2)
        print(f"В итоге вы получите {doxod} рублей")
        print(f"В итоге вы получите {round(doxod * 0.0123, 2)} долларов")
        print(f"В итоге вы получите {round(doxod * 0.0877, 2)} Юаней")
        return doxod


class GenerateName:
    def __init__(self):
        self.names = ["Игорь", "Вася", "Саша", "Артём", "Владислав", "Лев", "Александр", "Никита", "Юра"]
        self.second_names = ["Иванов", "Петров", "Сидоров", "Кайдалов", "Панченко", "Кудрявцев", "Никифоров", "Гаврилов", "Перепёлкин"]

    def Generate(self, printmode = False):
        name = random.choice(self.names)
        family_name = random.choice(self.second_names)

        if printmode == True:
            print(f"Имя героя - {name}")
            print(f"Фамилия героя - {family_name}")
            return name
        else:
            return name


class Menu:
    def __init__(self):
        self.build = []

    def Build(self, variant1, variant2, variant3):
        '''Build'''

        self.build.append([variant1])

        self.build.append([variant2])


        self.build.append([variant3])




        choise = input(f'1 - {self.build[0]} \n'
              f'2 - {self.build[1]} \n'
              f'3 - {self.build[2]} \n'
              f'4 - Выход \n'
              f'Ваш выбор >>> ')

        if choise == "1":
            return 1

        if choise == "2":
            return 2

        if choise == "3":
            return 3

        if choise == "4":
            exit()


class console:
    def __init__(self):
        self.bufer = ""
    
    def clear_last_line(self):
        """Очищает последнюю строку в консоли"""
        sys.stdout.write('\033[F') 
        sys.stdout.write('\033[K')
        sys.stdout.flush()
    
    def Print_animation_letters(self, text=""):
        for i in range(len(text) + 1):
            self.bufer = text[:i]
            print(self.bufer)
            if i < len(text):
                time.sleep(0.1)
                self.clear_last_line()

