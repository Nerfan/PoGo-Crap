"""
A few utilities to make my Pokemon Go life easier
"""

class Species():
    """
    Data about the current storage of a Pokemon

    IMPORTANT: This class does not represent a single Pokemon;
    rather, it represents the species as a whole and the numbers
    of individual Pokemon and candirs currently in storage.
    """
    def __init__(self, name, number, candy, candyreq):
        self.name = name
        self.number = number
        self.candy = candy
        self.candyreq = candyreq

    def transfer(self, number=1):
        """
        Simulate transferring an amount of Pokemon.

        This removes x Pokemon and adds x candy.

        Args:
            number (int): Number of Pokemon to transfer
        """
        self.number -= number
        self.candy += number

    def evolve(self):
        """
        Simulate evolving a Pokemon.
        """
        if self.candy < self.candyreq:
            return
        self.number -= 1
        self.candy -= (self.candyreq-1)

    def evolve_all(self):
        """
        Simulates transferring and evolving the max amount possible
        """
        self.transfer(calculate_equilibrium(
            self.candy,
            self.number,
            self.candyreq
        ))
        for i in range(calculate_max_evos(self.candy, self.candyreq)):
            self.evolve()

    def __str__(self):
        return self.name + " " + str(self.number) + " " + str(self.candy)

def calculate_max_evos(candy, candyreq):
    """
    Calculate the max number of Pokemon that can be evolved given n candy

    Args:
        candy (int): Amount of candy in possession
        candyreq (int): Amount of candy required to evolve a single Pokemon

    Returns:
        int: Number of pokemon that can be evoled with the given amounts
    """
    if candy <= candyreq:
        return 0
    evos = 1
    candy -= candyreq
    evos += candy//(candyreq-1)
    return evos

def calculate_equilibrium(candy, pokemon, candyreq):
    """
    Calculate how many pokemon should be transferred to achieve max evolutions

    Args:
        candy (int): Amount of candy in possession
        pokemon (int): Number of the type of Pokemon in possession
        candyreq (int): Amount of candy required to evolve a single Pokemon

    Returns:
        int: Number of pokemon that should be transferred
    """
    transfer = 0
    while pokemon > calculate_max_evos(candy, candyreq):
        pokemon -= 1
        candy += 1
        transfer += 1
    return transfer

weedle = Species("Weedle", 13, 144, 12)
weedle.evolve_all()
print(weedle)
