import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():  # name starting with '_' mean it isn't intended to be public
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))
            # # Account. is better than self. in this instance

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    ike = Account("Ike", 0)
    ike.show_balance()

    ike.deposit(1000)
    # ike.show_balance()
    ike.withdraw(500)
    # ike.show_balance()

    ike.withdraw(30000)

    ike.show_transactions()

    steph = Account("Steph", 800)
    steph.__balance = 200  # when name starts with 2 '_', the name is "mangled", it prevents shadowed var names
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    steph.show_balance()
    print(steph.__dict__)
    steph._Account__balance = 40
    steph.show_balance()
