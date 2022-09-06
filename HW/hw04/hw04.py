def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    if not lst1:
        return lst2
    elif not lst2:
        return lst1
    elif lst1[0]>lst2[0]:
        return [lst2[0]]+merge(lst1, lst2[1:])
    else:
        return [lst1[0]]+merge(lst1[1:], lst2)


class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2021
    >>> dime = mint.create(Dime)
    >>> dime.year
    2021
    >>> Mint.present_year = 2101  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Mint.present_year = 2176     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2021

    def __init__(self):
        self.update()

    def create(self, coin):

        return coin(self.year)
        "*** YOUR CODE HERE ***"

    def update(self):
        "*** YOUR CODE HERE ***" 
        self.year= self.present_year 


class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        return self.cents+max(Mint.present_year-self.year-50,0)
        "*** YOUR CODE HERE ***"


class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    
    quantity=0
    balance=0
    
    def __init__(self, product, price):
        self.price=price
        self.product=product
        
    def restock(self,quantity):
        self.quantity += quantity
        return f'Current {self.product} stock: {self.quantity}'
    
    def vend(self):
        if self.quantity==0:
            return f'Nothing left to vend. Please restock.'
        elif self.balance < self.price:
            return f'You must add ${self.price-self.balance} more funds.'
        else:
            self.balance -= self.price
            self.quantity -= 1
            if self.balance == 0:
                return f'Here is your {self.product}.'
            else:
                charge = self.balance
                self.balance = 0
                return f'Here is your {self.product} and ${charge} change.'


            
            

    def add_funds(self,money):

        if self.quantity==0:
            return f'Nothing left to vend. Please restock. Here is your ${money}.'
        else:
            self.balance += money
            return f'Current balance: ${self.balance}'