

# is_active = True
# is_logged_in = False

# print( 5 > 3)
# print( 10 == 2)


# x = 5
# print(type(x))

# y = 3.14
# print(type(y))

# name = "ali"
# print(type(name))

# flag = True
# print(type(flag))

# name = "Динара"
# age = 18

# print("привет")
# print(5 + 18)
# print("Меня зовут" , name)
# print(f"Мне {age} лет")


# name = input("Введите ваше имя :")
# print(f"Привет, {name}!")

# age = int(input("Введите ваш возраст :"))
# height = float(input("Введите ваш рост :"))
# print(f"{age}  {height}")




# + 

# -

# *

# /

# //

# %

# **


# ==

# !=

# >

# <

# >=

# <=


# and
# or 
# not



# if 
# elif 
# else
    

# if условие1:
#     # выполняется если условие true
# elif условие2:
#     # выполняется если условие false
# else:
#     #выполняется если все условие false


# age = int(input("Введите ваш возраст :"))

# if age < 12:
#     print("Ты ребенок")
# elif age < 18:
#     print("Ты подросток")
# else:
#     print("Ты взрослый")


# a = int(input("Введите число а :"))
# b = int(input("Введите число b :"))

# if a > 0 and b > 0:
#     print("Оба числа положительные")
# elif a > 0 or b > 0:
#     print("Хотя бы одно число положительное")
# else:
#     print("Оба числа неположительные")


# password = input("Введите пароль :")

# if password == "12345": 
#     print("Доступ разрешен")
# else: 
#     print("Доступ запрешен")



# name = input("Как тебя зовут?")
# age = int(input("Сколько тебе лет?"))
# language = input("Какой твой любимый язык программирования")

# if age < 12:
#     stage = "Ребенок"
# elif age < 18:
#     stage = "Подросток"
# else:
#     stage = "Взрослый"

# print(f"Привет, {name}! Ты {stage}.")
# print(f"Твой любимый язык: {language}")

# a = int(input("Введите число а :"))
# b = int(input("Введите число b :"))

# a = int(input("Введите число  :"))


# if a > 0:
#     print("положительные")
# elif a < 0:
#     print("отрицательный")
# else:
#     print("ноль")

# password = input("Вход в систему:")

# if password == "Барс": 
#     print("Доступ разрешен")
# else: 
#     print("Доступ запрешен")

# point = int(input("НУ ЧТО КАК ТЕБЕ?"))

# if point >= 90:
#     print("Отлично!")
# elif point >=75:
#    print("Хорошо")
# elif point >= 60:
#    print("Удовлетворительно")
# else:
#     print("Попробуй ещё раз")



# number = int(input("Введите число : "))

# if number > 0:
#     print("Положительное число")
# elif number < 0:
#     print("Отрицательное число")
# else:
#     print("ноль")


# password = "12345"

# user_input = input("Введите пароль : ")

# if user_input == password:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")


# grade1 = int(input("Введите первую оценку"))

# grade2 = int(input("Введите вторую оценку"))

# grade3 = int(input("Введите третью оценку"))

# average = (grade1 + grade2 + grade3) /3
# print(f"Средний балл: {average}")

# if average >= 90:
#     print("Отлично")
# elif average >= 75:
#     print("хорошо")
# elif average >=60:
#     print("удовлетворительно")
# else:
#     print("попробуй еще раз")


# print ("=== prostoi kalkylator===")

# a = float(input("vedite pervoe chislo :"))
# b = float(input("vedite wtoroe chislo :"))
# operation = input("Wedite operaziy (+ ,- , * , / )")

# if operation == "+":
#     print("resyltat : ", a+b )
# elif operation == "-":
#     print("resyltat : ", a-b )
# elif operation == "*":
#     print("resyltat : ", a*b )
# elif operation == "/":
#     if b != 0:
#         print("resyltat :", a / b)
#     else:
#         print("ochibka: ne deli na nol idiot😡 !")
# else:
#     print("ochibka:idiot normalno pichi🤦‍♂️ !")

# for i in range(1, 10):
#     if i % 2 == 0:
#         continue
#         print(i)

# for i in range(10):
#     print("Привет")


# for переменая in последвательность:
#     # тело цикла

# for i in range(5):
#     print("Цикл", i)

# for i in range(1, 11):
#     print(i)


# word = "Python"
# for letter in word:
#     print(letter)


# while условие:
#     # тело цикла

# i = 1
# while i <= 9:
#     print("счет", i)
#     i += 1




# while True:
#     print("я буду выполняться вечно")


# password = ""
# while password != "python":
#     password = input("Введите пароль : ")
# print("Доступ разрешен")


# for san in range(10):
#     if san == 5:
#         break
#     print(san)

# for i in range(6):
#     if i == 3:
#         continue
#     print(i)


# total = 0
# for i in range(1, 101):
#     total += i
# print("Сумма чисел от 1 до 100", total)

# for i in range(1, 10):
#     if i % 2 == 0:
#         print("Первое четное", i)
        

# for i in range(1, 10):
#     if i % 2 == 0:
#         continue
#     print(i)

# print("=== программа Угадай число ===")
         
# secret = 7
# guess = 0

# while guess != secret:
#     guess = int(input("Введите число от 1 до 10 : "))
#     if guess < secret:
#         print("Мало")
#     elif guess > secret:
#         print("Много")
#     else:
#         print("Верно")




# for i in range(1, 21):
#     if i == 5 or i == 10:
#         continue
#     print(i)


# num = int(input("vedite chislo:"))
# for i in range(1, 10):
#     print(f"{num} * {i} == {num * i}")

# password = ""

# while password != "Bars":
#     password = input("vedite parol: ")

#     if password != "Bars":
#         print("neverno!")




# Zadacha1

# number = int(input("vedite chislo"))
# for i in range(1, number):
#     print(i)

# total = 0
# for i in range(1, 101):
#     total += i
# print("Сумма чисел от 1 до 100", total)


# N = int(input("vedite chislo: "))

# for i in range(1, N + 1):
#     if i % 2 == 0:
#     print(i)


# num = int(input("vedite chislo:"))
# for i in range(1, 10):
#     print(f"{num} * {i} == {num * i}")


# num = int(input("Введите число: "))
# i = 1
# while i <= 10:                    
#     print(f"{num} * {i} = {num * i}")
#     i += 1               

# for i in range(0, 20 ,3):
#     print(i)




# word = "python"
# for letter in word:
#     print(letter)

# while условие:
#     # тело цикла


# i = 1

# while i < 10:
#     print(i)
#     i += 1

# while True:
#     print(1)

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)


# text = "Он сказал : \"Привет\""
# print(text)


# word = "python"

# print(word[::2])


# print()
# input()
# len()
# .upper() все буквы в верхний регистр
# .lower() все буквы в нижный регистр
# .title() каждое слово с заглавной
# .strip() удаляет пробелы по краям
# .replace(a , b) заменяеи a на b
# .split() разбивает строку в список
# .join() собирает строку  из списка

# text = "привет мир"
# print(text.split(","))

# name = "Алина"
# age = 18
# print("Меня зовут" + name + ". мне " + str(age) + "лет")
# print(f"меня зовут {name}. мне {age} лет")
# text = "pythonkljbdfhbodsjciohdsuighdsoicvjuidsHTIODFJIOVHDFSUIGJPODFHBIUDFGOPJDFH9UVBHSDFOIJG"
# print(len(text))


















   # #                       Изменяемый          Упорядоченный
    
# list   список     []          да                  да
# tuple  кортеж     ()          нет                 да
# set    множество  {}          да                  нет
# dict   словарь    {}          да                  да(ключи уникальны)
   










# fruits = ["apple", "banana", "orange"]
# print(fruits[0])
# print(len(fruits))

# fruits.append("mango")
# fruits.remove("banana")
# fruits.sort()
# print(fruits)


# data = (10, 20, 30)
# print(data[1])

# nums = {1,2,3,3,2,1}
# print(nums)


# user = {
#     "name": "Anima",
#     "age": 18,
#     "city": "Bishkek"
# }

# print(user["name"])
# user["age"] = 19
# user["job"] = "dev"
# print(user)














# gorod = ["Bishkek", "Osh", "Karakol"]


# gorod.append("Naryn")   
# gorod.remove("Osh")
# gorod.sort()
# print(gorod)

# number = (10, 20, 30, 40)
# print(number[3])


# nums = {1,2,3,3,2,1,1,3,4,2,4,5,5,2,4,5,2,2,4,}
# print(nums)

# user = {
#     "name":"Ali",
#     "age":17,
# }


# print(user["name"])
# user["age"] = 18
# user["contru"] = "Kyrsctan"
# print(user)


# 第月, [24.10.2025 16:22]
# n = int(input("Введите число : "))
# count = 0
# m = abs(n)
# while m > 0:
#     m //= 10
#     count += 1
# print("Колличество цифр : " , count if n != 0 else 1)

# 第月, [24.10.2025 16:28]
# n = int(input("Ввести число :"))
# s = 0
# for digit in str(abs(n)):
#     s += int(digit)
# print("сумма цифр", s)

# 第月, [24.10.2025 16:34]
# n = int(input("ввести число : "))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(factorial)

# 第月, [24.10.2025 16:37]
# s = input("Ввести строку")
# for i in range(len(s)):
#     print(i, "->", s[i])

# 第月, [24.10.2025 16:42]
# s = input("Ввести строку:").lower()
# vowels = "aeiouyаиоуэяюеы"
# count = 0

# for char in s:
#     if char in vowels:
#         count += 1
# print("главсных букв" , count)

# 第月, [24.10.2025 16:52]
# n = int(input("Введите n: "))
# a, b = 1,1
# for i in range(n):
#     print(a, end=" ")
#     a , b = b , a + b

# 第月, [24.10.2025 17:34]
# file = open("data.txt", "r")

# "r" чтение
# "w" запись
# "a" добавление
# "x" создает новый файл

# f = open("data.txt", "r")
# text = f.read()
# print(text)
# f.close()

# with open("data.txt", "r") as f:
#     text = f.read()
#     print(text)

# with open("data.txt", "w") as f:
#     f.write("hello world")

# with open ("data.txt", "a") as f:
#     f.write("\n new page")

# with open("data.txt", "r") as f:
#     for line in f:
#         print(line.strip())


# try:
#     x = 10 / 0
# except:
#     print("Ощибка! на ноль делить нельзя")


# try:
#     num = int(input("Введите число:"))
# except ValueError:
#     print("Ощибка: введите именно Число")

# try:
#     f = open("file.txt")
#     print(f.read())
# except FileNotFoundError:
#     print("Файл не найден")
# finally:
#     print(" Программа завершена")



# try:
#     f= open ("зва")
#     print(f.read())
# except FileNotFoundError:
#     print("Ошибка:возраст должен быть ЧИСЛОМ!")
# finally:
#     print("пользователь успешно сохраниен!")



















# products = {
#     "1": ("TANG", 45000),
#     "2": ("Snikers", 30000),
#     "3": ("USE BOMBA", 5000),
#     "4": ("DVD", 20000),
#     "5": ("BUGATI", 3500),
#     "6": ("KET", 2500),
#     "7": ("MANGO", 1500),
# }

# cart = []
# while True:

#     print("1 — Показать товары")
#     print("2 — Добавить товар в корзину")
#     print("3 — Показать корзину")
#     print("4 — Удалить товар из корзины")
#     print("5 — Сформировать чек и выйти")
#     print("0 — Выход без покупки")

#     choice = input("Выберите действие: ")

#     if choice == "1":
#         print("Доступные товары:")
#         for key, value in products.items():
#             print(f"{key}. {value[0]} — {value[1]} сом")

#     elif choice == "2":
#         product_id = input("Введите номер товара: ")
#         if product_id in products:
#             cart.append(products[product_id])
#             print(f"Товар '{products[product_id][0]}' добавлен в корзину.")
#         else:
#             print("Ошибка: товара с таким номером нет.")

#     elif choice == "3":
#         if not cart:
#             print("Корзина пуста.")
#         else:
#             print("--- Ваша корзина ---")
#             total = 0
#             for item in cart:
#                 print(f"{item[0]} — {item[1]} сом")
#                 total += item[1]
#             print(f"ИТОГО: {total} сом")

#     elif choice == "4":
#         if not cart:
#             print("Корзина пуста")
#         else:
#             print("--- Корзина ---")
#             for i, item in enumerate(cart, start=1):
#                 print(f"{i}. {item[0]} — {item[1]} сом")
#             try:
#                 remove_index = int(input("Введите номер товара: "))
#                 if 1 <= remove_index <= len(cart):
#                     removed = cart.pop(remove_index - 1)
#                     print(f"Товар '{removed[0]}' удалён из корзины.")
#                 else:
#                     print("Ошибка: неправильный номер.")
#             except ValueError:
#                 print("Ошибка: нужно ввести число.")
    
#     elif choice == "5":
#         print("--- ЧЕК ---")
#         if not cart:
#             print("Корзина пуста.")
#         else:
#             total = 0
#             for item in cart:
#                 print(f"{item[0]} — {item[1]} сом")
#                 total += item[1]
#             print(f"ИТОГО К ОПЛАТЕ: {total} сом")
#         break
#     else:
#         print(" Неверный выбор, попробуйте снова.")







# print()
# input()


# def имя фунции ():
#     #код    

# имя функции()

# def say_hello():
#     print("Привет")

# say_hello()




# def greet(name):
#     print(f"Привет, {name}")


# greet("Азамат")
# greet("мирлан")
# greet("айбек")
# greet("исмар")
# greet("адилет")
# greet("Ома")


# def plus(a, b):
#     return a + b

# result = plus(3, 5)

# print(result)


# def greet(name = "Гость"):
#     print(f"Привет, {name}")

# greet()
# greet("Нинзя")


# def greet(n):
#     f = 1
#     for i in range(1, n + 1):
#         f = f * i
#     return f









# def greet(name):
#     print(f"Привет, {name}")


# greet("Азамат")
# greet("мирлан")
# greet("айбек")
# greet("исмар")
# greet("адилет")
# greet("Ома")

# def plus(a, b):
#     return a + b

# result = plus(3, 5)

# print(result)










# def greet(name):
#     print(f"Привет, {name}!")
# greet("Барс")



# def squar(num):
#     return num ** 2
# print(squar(5))  



# def fact(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print(fact(5))  



# def count(text):
#     a = "а,е,ё,и,о,у,ы,э,ю,я"
#     b = 0
#     for a in b.lower():
#         if a in b:
#             count += 1
#     return count
# print(count("Привет"))  






# def isit(num):
#     s = str(num)
#     return s == s[::-1]


# print(isit(1221))  
# print(isinstance(1234))  



# def имя функции():
#     # тело функции


# def hello(name):
#     print("привет", {name})


# hello("alina")

# def plus(a, b):
#     return a + b

# result = plus(1,2)
# print(result)


# def greet(name = "гость"):
#     print(f"привет , {name}")

# greet()
# greet("alina")


#*args - собирает любое колличество аргументов Кортежа

# def total(*numbers):
#     print(numbers)

# total(1,2,3,4,5,5,5)

# def total(*numbers):
#     return sum(numbers)

# print(total(10,20,30))

#**kwargs - собирает любые Именованные аргументы в словарь

# def info(**data):
#     print(data)

# info(name = "Asel", age=20, country = "KG")

# square = lambda x: x * x

# print(square(5))


# def check_password(password):
#     return len(password) >= 8

# user_input = input("Введите пароль :")
# if check_password(user_input):
#     print("пароль надежный")
# else:
#     print("парoль слишком короткий")



# def delivery_cost(*prices):
#     return sum(prices) + 300* 3

# print(delivery_cost(2000, 2000, 75000))


# def create_text(**info):
#     text = "Здравствуйте"
#     if "name" in info:
#         text += f"{info['name']}"
#     else:
#         text += "!"

#     if "city" in info:
#         text += f"мы видим, что вы из города {info['city']}"
    
#     return text

# print(create_text(name="alina", city="bishkek"))
# print(create_text(name="nurdoolot", city="osh"))


# users = [('azamat', 17), ('diana', 20), ('aibek', 19)]

# users_sorted = sorted(users, key= lambda user:user[1])
# print(users_sorted)


















# def translate(word, lang="ru"):
#     if lang == "ru":
#         return "Привет"
#     elif lang == "en":
#         return "Hello"
#     elif lang == "kg":
#         return "Салам"
#     else:
#         return "Язык не поддерживается"
       
# print(translate("hi", "en"))   
# print(translate("hi", "kg"))   
# print(translate("hi", "fr"))  


