'''Подвиг 8. Объявите в программе класс Cart (корзина), объекты которого создаются командой:

cart = Cart()
Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки (объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.

В классе Cart объявить методы:

add(self, gd) - добавление в корзину товара, представленного объектом gd;
remove(self, indx) - удаление из корзины товара по индексу indx;
get_list(self) - получение из корзины товаров в виде списка из строк:

['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']

Объявите в программе следующие классы для описания товаров:

Объекты этих классов должны создаваться командой:

gd = ИмяКласса(name, price)
Каждый объект классов товаров должен содержать локальные свойства:

name - наименование;
price - цена.

Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами.

P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям.'''


class Cart:
    def __init__(self, goods):
        goods = []
        self.goods = goods

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        pass

    def get_list(self):
        pass


def create_product(self, name, price):
    self.name = name
    self.price = price


class Table:
    create_product()


class TV:
    create_product()


class Notebook:
    create_product()


class Cup:
    create_product()


cart = Cart()