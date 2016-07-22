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
        temp = self.calculate_max_evos()
        evos = temp[0]
        transfers = temp[1]
        self.transfer(transfers)
        for i in range(evos):
            self.evolve()

    def calculate_max_evos(self):
        """
        Calculate the maximum number of evolutions possible

        Returns:
            tuple (int, int): Maximum number of evolutions possible
                              Max number of Pokemon to transfer
        """
        poketemp = self.number
        candytemp = self.candy
        while poketemp > (candytemp-1)//(self.candyreq-1):
            poketemp -= 1
            candytemp += 1
        return (
            min((candytemp-1)//(self.candyreq-1), poketemp),
            self.number-poketemp
            )

    def __str__(self):
        return self.name + " " + str(self.number) + " " + str(self.candy)

pokemon = [
    Species("Weedle", 12, 136, 12),
    Species("Caterpie", 1, 12, 12),
    Species("Pidgey", 25, 191, 12),
    Species("Rattata", 13, 184, 25),
    Species("Spearow", 5, 107, 50),
    ]
for pokemon in pokemon:
    print(pokemon.calculate_max_evos())
