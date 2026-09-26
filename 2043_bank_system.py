class Bank:

    def __init__(self, balance: list[int]):
        self.balance = {}
        for i, v in enumerate(balance, start=1):
            self.balance[i] = v

    def ifvalid(self, account_id):
        return account_id in self.balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.ifvalid(account1) and self.ifvalid(account2) and money <= self.balance[account1]:
            self.balance[account1] -= money
            self.balance[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.ifvalid(account):
            self.balance[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.ifvalid(account) and money <= self.balance[account]:
            self.balance[account] -= money
            return True
        return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)



