import random
import string


def generate_random_email():
    letters = string.ascii_lowercase
    number_last_name = random.randint(5, 15)
    name_patronymic = ''.join(random.sample(letters, 2))
    last_name = ''.join(random.sample(letters, number_last_name))
    digits_for_email = random.randint(100, 999)
    return f'{name_patronymic}.{last_name}{digits_for_email}@yandex.ru'
