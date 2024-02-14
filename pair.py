class Pair():
    def __init__(self, original_currency: str, to: str):
        self.original_currency = original_currency
        self.to = to

    def __eq__(self, pair_2):
        return self.original_currency == pair_2.original_currency and self.to == pair_2.to
    
    def __hash__(self) -> int:
        return 0