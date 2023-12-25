class Expense:

    def __init__(self, name: str, category: str, amount: float) -> None:
        self.name: str = name
        self.category: str = category
        self.amount: float = amount
        
    def __repr__(self) -> str:
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}>"
