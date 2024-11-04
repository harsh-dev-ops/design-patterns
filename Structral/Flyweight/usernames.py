import random
import string
from faker import Faker

faker = Faker()


class User:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class FlyweightUser:
    name_words = []

    def __init__(self, name: str):
        self.__name_indices = [self.__get_or_add_name_word(
            name_word) for name_word in name.split()]

    def __get_or_add_name_word(self, name_word: str):
        if name_word in self.name_words:
            return self.name_words.index(name_word)
        else:
            self.name_words.append(name_word)
            return len(self.name_words) - 1

    @property
    def name(self):
        # print(self.__name_indices)
        return ' '.join([self.name_words[i] for i in self.__name_indices])

    def __str__(self) -> str:
        return self.name


def genral_user_name_combination_count(all_user_names: list[str]):
    real_word_count = 0
    name_set = set()
    for user_name in all_user_names:
        real_word_count += len(user_name.split())
        for name_word in user_name.split():
            if name_word not in name_set:
                name_set.add(name_word)

    return len(name_set), real_word_count


def normal_user_name_combination_count(users: list[User]):
    all_user_names = [user.name for user in users]

    ideal_word_count, real_word_count = genral_user_name_combination_count(
        all_user_names)

    print("\nWithout Flyweight")
    print(f'Ideal word count: {ideal_word_count}')
    print(f'Real word count: {real_word_count}')
    # print(f'No. of repeated Words: {real_word_count - ideal_word_count}')
    print(f'Answer: {real_word_count == ideal_word_count}')


def flyweight_user_name_combination_count(users: list[FlyweightUser], all_user_names: list[str]):
    ideal_word_count, _ = genral_user_name_combination_count(
        all_user_names)

    real_word_count = len(users[0].name_words)
    print("\nWith Flyweight")
    print(f'Ideal word count: {ideal_word_count}')
    print(f'Real word count: {real_word_count}')
    # print(f'No. of repeated Words: {real_word_count - ideal_word_count}')
    print(f'Is Ideal word count eual to real word count?')
    print(f'Answer: {real_word_count == ideal_word_count}')


def random_user_name():
    name = faker.name()
    full_name = name
    if len(name.split()) == 3:
        first_name, last_name, _ = name.split()
        full_name = first_name + ' ' + last_name
    return full_name


if __name__ == '__main__':
    users = []
    names = [random_user_name() for _ in range(1000)]

    for name in names:
        users.append(User(name))

    normal_user_name_combination_count(users)

    flyweight_users = []
    for name in names:
        flyweight_users.append(FlyweightUser(name))

    flyweight_user_name_combination_count(flyweight_users, names)
