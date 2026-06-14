# print("Hello, World!")
# print("Welcome to the world of programming!")
# print("This is a simple Python program.")

# print("Let's do some basic arithmetic:")
# a = input("Enter a number: ")
# b = input("Enter another number: ")
# a = int(a)
# b = int(b)
# c = a + b   
# print(f"The sum of {a} and {b} is: {c}")

# a = float(input("Введіть сторону квадрата a: "))
# P = 4 * a
# print(f"Периметр квадрата дорівнює {P}")

# sentence_one = "Hello world"
# sentence_two = "Hello " + "world"
# # Відображення змінних
# print(sentence_one, sentence_two, sep='\n')

# # Перевірка рівності і ідентичності
# print(f'Are sentence equal? {sentence_one == sentence_two}')
# print(f'Are sentence identical? {sentence_one is sentence_two}')

# # Перевірка місця збереження у памяті
# print(f'Path of sentence in memory {id(sentence_one)}')
# print(f'Path of sentence in memory {id(sentence_two)}')

FLOORS = 30
APARTMENTS_PER_FLOOR = 3

apartment_number = int(input('Enter apartment number: '))
apartments_per_entrance = FLOORS * APARTMENTS_PER_FLOOR
entrance_number = (apartment_number - 1) // apartments_per_entrance + 1
floor_number = ((apartment_number - 1) % apartments_per_entrance) // APARTMENTS_PER_FLOOR + 1
print(f"Entrance number {entrance_number}, Floor number {floor_number}")