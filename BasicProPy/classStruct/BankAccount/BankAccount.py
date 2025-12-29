class BankAccount:

    def __init__(self, name: str):
        self._name = name
        self._balance = 0.0  

    @property
    def name(self) -> str:
        return self._name

    @property
    def balance(self) -> float:
        return self._balance


    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
        

    def withdraw(self, amount: float):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            
    def __str__(self) -> str:
        return f"Account Name: {self.name}, Balance: ${self.balance:.2f}"