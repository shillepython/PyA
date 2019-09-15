class pitomec(object):
    total = 0
    @staticmethod
    def status():
        print('Общие число зверюшек ', str(pitomec.total))

    def __init__(self, name, hunder = 10, boredom = 5):
        self.__name = name
        self.hunder = hunder
        self.boredom = boredom
        pitomec.total += 1

    def __str__(self):
        ans = '======================\n'
        ans += 'Объект класса pitomec\n'
        ans += 'Имя: ' + self.name
        return ans

    def __past_time(self):
        self.hunder += 1
        self.boredom += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print('Имя успешно изменено.')

    @property
    def mood(self):
        unhuppened = self.hunder + self.boredom
        if unhuppened < 5:
            m = "Отлично"
        elif 5 <= unhuppened <= 10:
            m = "Неплохо"
        elif 11 <= unhuppened <= 15:
            m = "Не сказать что хорошо"
        else:
            m = "Ужасно"
        return m

    def tolk(self):
        print("Привет.Меня зовут", self.name, " и я себя чувствую:", self.mood)
        self.__past_time()

    def eat(self, food = 4):
        print("Мррр...Спасибо!")
        self.hunder -= food
        if self.hunder < 0:
            self.hunder = 0
        self.__past_time()

    def play(self, fun = 4):
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__past_time()

def main():
    crit1 = pitomec('Фантик1')
    crit2 = pitomec('Фантик2')
    crit3 = pitomec('Фантик3')
    
    pitomec.status()
    crit1.tolk()
    print(crit1)
    print('Голод: ' + str(crit1.hunder))
    print('Усталось: ' + str(crit1.boredom))
    print('Настроение: ' + str(crit1.mood))

    crit1.eat()
    crit1.play()
    
    print('Настроение: ' + str(crit1.mood))
    print('======================')
main()