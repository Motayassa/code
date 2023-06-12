'''- приватная локальная переменная money (целочисленная) для хранения количества денег
(своя для каждого объекта класса Money);
- публичный метод set_money(money) для передачи нового значения приватной локальной переменной money
(изменение выполняется только если метод check_money(money) возвращает значение True);
- публичный метод get_money() для получения текущего объема средств (денег);
- публичный метод add_money(mn) для прибавления средств из объекта mn класса Money к средствам текущего
объекта;
- приватный метод класса check_money(money) для проверки корректности объема средств в параметре money
(возвращает True, если значение корректно и False - в противном случае).

Проверка корректности выполняется по критерию: параметр money должен быть целым числом, больше или 
равным нулю.'''


class Money:
    def __init__(self, mn):
        self.__money = mn

    def set_money(self, money):
        pass

    def get_money(self):
        pass

    def add_money(self, mn):
        pass

    def __check_money(self, money):
        return type(money) == int and money >= 0
