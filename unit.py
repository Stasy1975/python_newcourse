# # Введення (отримання даних)
# ім_я = input("Введіть ваше ім'я: ")

# # Перетворення (обробка даних)
# вітання = f"Привіт, {ім_я}!"

# # Виведення (виведення даних)
# print(вітання)

# age = 15
# is_adult = age >= 18  # True
# print(f"Чи є людина повнолітньою? {is_adult}")

# s1 = "Hello"
# s2 = "world!"
# joined_string = s1 + " " + s2
# print(joined_string)

# n = 5000

# hours = n // (60 * 60)
# minutes = (n - hours * 60 * 60) // 60
# seconds = n - hours * 60 * 60 - minutes * 60
# print(f"{n} секунд - це {hours} годин, {minutes} хвилин і {seconds} секунд.")

# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# print(my_dict["name"])  # Виведе 'Alice'
# my_dict["age"] = 26  # Змінює вік на 26
# my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
# print(my_dict)
# del my_dict["age"]
# print(my_dict)

# print("name" in my_dict)
# print("age" in my_dict)

# my_dict = {"name": "Alice", "age": 25}
# age = my_dict.get("age")  # Поверне 25
# gender = my_dict.get("gender")  # Поверне None, оскільки "gender" немає в словнику
# print(f"Age: {age}, Gender  : {gender}")

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.difference(b))  # {1, 2}
# print(a - b)  # {1, 2}


# # Просте форматування рядка
# name = 'John'
# print('Hello, {}!'.format(name))

# # Форматування з декількома аргументами
# age = 25
# print('Hello, {}. You are {} years old.'.format(name, age))

# # Використання іменованих аргументів
# print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# # Використання індексів для вказівки порядку аргументів
# print('Hello, {1}. You are {0} years old.'.format(age, name))

# x = int(input("X: "))
# y = int(input("Y: "))

# if x == 0:
#     print("X can`t be equal to zero")
#     x = int(input("X: "))

# result = y / x


# # Зчитування рядка від користувача
# user_input = input("Введіть рядок: ")

# # Ініціалізація змінних для підрахунку символів та пробілів
# total_chars = len(user_input)  # загальна кількість символів у рядку
# space_count = 0  # кількість пробілів

# # Підрахунок кількості пробілів
# for char in user_input:
#     if char == " ":
#         space_count += 1

# # Виведення результатів
# print(f"Загальна кількість символів у рядку: {total_chars}")
# print(f"Кількість пробілів у рядку: {space_count}")

# some_list = ["apple", "banana", "cherry"]
# for index in enumerate(some_list):
#     print(index, value)


# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник  
#             codes[ch] = ord(ch)  
#     return codes
# result = string_to_codes("Фантомас")
# print(result)


# x = 50

# def func() -> None:
#     x = 2
#     print('Зміна локального x на', x)  # Зміна локального x на 2

# func()
# print('Глобальний x як і раніше', x)  # x як і раніше 50

# def say(message, times=1):
#     print((message + " ") * times)

# say('Привіт') 
# say('Світ', 5)

# def factorial(n):
#     if n == 0: # базовий випадок
#         return 1
#     else:
#         return n * factorial(n-1) # рекурсивний випадок

# print(factorial(100)) # виведе 120


def factorial(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Повернення результату для n = ", n, ": ", result)
        return result

print(factorial(5))
