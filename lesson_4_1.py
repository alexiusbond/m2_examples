from random import randint
from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        pass

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.name} health: {self.health} [{self.damage}]'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability_type):
        super().__init__(name, health, damage)
        self.__super_ability_type = super_ability_type

    @property
    def super_ability_type(self):
        return self.__super_ability_type

    @super_ability_type.setter
    def super_ability_type(self, value):
        self.__super_ability_type = value

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = randint(2, 5)
        boss.health -= self.damage * coeff
        print(f'Warrior hits critically: {self.damage * coeff}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        print(f'Medic {self.name} healed')
        for h in heroes:
            if self != h and h.health > 0:
                h.health += self.__heal_points


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        print('Magic boosted')
        boost = randint(1, 5)
        for h in heroes:
            if h.health > 0:
                h.damage += boost


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)

    def apply_super_power(self, boss, heroes):
        pass


round_number = 0


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for h in heroes:
        if h.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def print_statistics(boss, heroes):
    print(f'{round_number} ROUND ----------')
    print(boss)
    for h in heroes:
        if (h.super_ability_type == SuperAbility.BOOST):
            print(h, 'I am very powerful magician!')
        else:
            print(h)


def boss_hits(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            h.health -= boss.damage


def heroes_hit(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            boss.health -= h.damage


def heroes_power(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            h.apply_super_power(boss, heroes)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss_hits(boss, heroes)
    heroes_hit(boss, heroes)
    heroes_power(boss, heroes)
    print_statistics(boss, heroes)


def start():
    boss = Boss('Tanos', 2000, 50)
    warrior = Warrior('Capitan America', 260, 10)
    medic = Medic('Doctor Strange', 250, 5, 15)
    assistant_of_medic = Medic('Aibolit', 260, 10, 5)
    magic = Magic('Saruman', 270, 15)
    berserk = Berserk('Bers', 280, 20)
    heroes = [warrior, medic, assistant_of_medic, magic, berserk]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start()
