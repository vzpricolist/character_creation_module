from random import randint

# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().
#from graphic_arts.start_game_banner import run_screensaver

# Стандартная атака — новая глобальная константа.
DEFAULT_ATTACK = 5
#стандартная защита
DEFAULT_DEFENCE = 10
#
DEFAULT_STAMINA = 80

class Character:
    
    #
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    #Диапазон атаки.
    RANGE_VALUE_ATTACK = (1, 3)
    #Диапазон защиты
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'


    # Объявляем конструктор класса.
    def __init__(self, name):
        self.name = name


   # Объявляем метод атаки
    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK);
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')


    # Объявляем метод защиты.
    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')
    

    # Объявляем метод специального умения.
    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    #Возвращает описание классов
    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'

class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'

class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


#Функция выбора персонажа
def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """
    # Добавили словарь, в котором соотносится ввод пользователя и класс персонажа.
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    
    approve_choice: str  = None
    
    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        # Вывели в терминал описание персонажа.
        
#        print(char_class.name)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    # Замените конструкцию условных операторов на словарь.
    common =       {'Warrior': Warrior, 'Mage': Mage, 'Healer': Healer,
                    'attack': character.attack, 'defence': character.defence,
                    'special':character.special}
#    game_classes = {'Warrior': ', ты Воитель — великий мастер ближнего боя.', 
#                    'Mage': ', ты Маг — превосходный укротитель стихий.', 
#                    'Healer': ', ты Лекарь — чародей, способный исцелять раны.'}

    print(character.__class__.__name__, common[character.__class__.__name__].BRIEF_DESC_CHAR_CLASS)
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')

#    command = {'attack': character.attack, 'defence': character.defence,'special':character.special}

    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        # Вместо блока условных операторов добавьте условие
        # принадлежности введённой команды словарю.
        # В функции print() будет вызываться метод класса,
        # который соответствует введённой команде.

        if cmd in common:
            print(common[cmd]())
        
    return 'Тренировка окончена.'

warrior = Warrior('Кодослав')
print(warrior)
print(warrior.attack())
#print(start_training(choice_char_class('Кодослав')))