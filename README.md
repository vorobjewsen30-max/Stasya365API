# Stasya365API
Интеграция сервисов Stasya365 в ваш код python
# Использование
![Интеграция](https://lh3.googleusercontent.com/pw/AP1GczPOWCNp8z8A9k6gWljd12_v0GswaZDVZVv3NzPX_xuBuMGq7niMHJMRBN4g867xEcC_DK3ZYZDE7GwyGx9IMQ59LqSoRltmUivvhWJexm4OytZi1iGLdJrtzttyYb8uZGi0Ke9wMgd7ZQK7kPC-Rw0=w1547-h919-s-no-gm?authuser=0)

- [X] Легко использовать
## Пример использования
```python
import Stasya365_API
import time
import functions
notes = Stasya365_API.notes()
functions.ravno_otdel(20)
Stasya365_API.console().Print_animation_letters(text="Добро пожаловать в text os. Зарегистрируйтесь для продолжения")
functions.ravno_otdel(20)
id = Stasya365_API.id()
id.registration()
name = id.Call_Back(objekt="login")
password = id.get_password(login=name)
time.sleep(1)
Stasya365_API.console().Print_animation_letters(text=f"Привет, {name}")
time.sleep(1)
print("Спасибо за вход")
menu = Stasya365_API.Menu()
while True:
    retern = menu.Build(variant1="Генератор персонажа", variant2="Работа", variant3="Жизнь")
    if retern == 1:
        time.sleep(1)
        Stasya365_API.GenerateName().Generate(printmode=True)
        time.sleep(1)
    if retern == 2:
        menu = Stasya365_API.Menu()
        retrn2 = menu.Build(variant1="Перевод числа в римское", variant2="Счёт увеличения микроскопа", variant3="Математика")
        if retrn2 == 1:
            Stasya365_API.math().to_rimsk()
        
        elif retrn2 == 2:
            Stasya365_API.Microscop().Count(printmode=True)

        elif retrn2 == 3:
            retern3 = Stasya365_API.Menu().Build(variant1="Счёт периметра", variant2="Счёт площади", variant3="Счёт суммы цифр")
            if retern3 == 1:
                Stasya365_API.math().count_p()

            elif retern3 == 2:
                Stasya365_API.math().count_S()

            elif retern3 == 3:
                Stasya365_API.math().count_summa()

    
    if retern == 3:
        ret = Stasya365_API.Menu().Build(variant1="Заметки", variant2="Считать доход с вклада", variant3="Посчитать будет ли гот високосный")
        if ret == 1:
            while True:
                notes.menu()
        
        if ret == 2:
            Stasya365_API.Vklad().count()
        
        if ret == 3:
            Stasya365_API.visokosni_god().count()


```

