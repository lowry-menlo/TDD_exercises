from __future__ import annotations
from abc import abstractmethod
from  expression import Expression


class Money(Expression):
    def __init__(self, initial_value: int, currency: str):
        self._amount = initial_value
        self._currency = currency
    
    def __eq__(self, money_obj):
        return type(self) == type(money_obj) and self._amount == money_obj._amount and self._currency == money_obj._currency
    

    def _currency(self):
        return self._currency

    def times(self, multiplier: int):
        return Money(self._amount * multiplier, self._currency)
    
    def plus(self, addend):
        return Sum(self, addend)
    
    
    @staticmethod
    def dollar(amount: int):
        return Money(amount, "USD")
    
    @staticmethod
    def franc(amount: int):
        return Money(amount, "CHF")
    

class Bank():
    def reduce(self, source: Expression, to: str):
        if (isinstance(source, Money)):
            return source
        sum:Sum = source
        return sum.reduce(to)
        # return source.reduce(to)
    

class Sum(Expression):
    def __init__(self, augend:Money, addend:Money):
        self.augend = augend
        self.addend = addend

    def reduce(self, to: str):
        amount:int = self.augend._amount + self.addend._amount
        return Money(amount, to)

    
