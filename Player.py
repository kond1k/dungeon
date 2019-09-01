class Player:
    achivment = []

    def __init__(self):
        self.name = input('Введите ваше имя \n')
        self.age = input('Введите ваш возраст \n')

    def get_name(self):
        return self.name
