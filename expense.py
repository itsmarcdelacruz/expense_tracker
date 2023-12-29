class Expense:

    def __init__(self, date:str, name: str, category: str, amount: float) -> None:
        self.name: str = name
        self.category: str = category
        self.amount: float = amount
        self.date: str = date
        
    def __repr__(self) -> str:
        return f"<Expense: {self.date}, {self.name}, {self.category}, ${self.amount:.2f}>"
