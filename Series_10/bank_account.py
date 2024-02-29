class BankAccount:
    """
    >>> b1 = BankAccount('Jan Jansen', '001457894501', 10000)
    >>> b2 = BankAccount('Peter Peeters', '842457894511', 10000)
    >>> b1.deposit(250)
    >>> b1.withdraw(1000)
    >>> b2.withdraw(300)
    >>> str(b1)
    'Jan Jansen, 001457894501, amount: 9250'
    >>> print(b2)
    Peter Peeters, 842457894511, amount: 9700
    >>> repr(b2)
    "BankAccount('Peter Peeters', '842457894511', 9700)"
    >>> b3 = BankAccount('David Davidse', '002457896312')
    >>> b3.deposit(112)
    >>> print(b3)
    David Davidse, 002457896312, amount: 112
    >>> b3
    BankAccount('David Davidse', '002457896312', 112)
    """
    def __init__(self, holder_name, account_number, money=0):
        self.holder_name = holder_name
        self.account_number = account_number
        self.money = money

    def __str__(self):
        return f'{self.holder_name}, {self.account_number}, amount: {self.money}'

    def __repr__(self):
        return f"BankAccount('{self.holder_name}', '{self.account_number}', {self.money})"

    def deposit(self, n):
        self.money = self.money + n

    def withdraw(self, n):
        self.money = self.money - n


if __name__ == '__main__':
    import doctest
    doctest.testmod()