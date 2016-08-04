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
        Simulate transferring and evolving the max amount possible
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
                              Minimum number of Pokemon to transfer
        """
        poketemp = self.number
        candytemp = self.candy
        # Go to the number of candies required for the next evolution
        # e.g. If we currently have 13 candies for a 12-candy evolution,
        #      we see if transferring 10 Pokemon would still allow us 2 left
        currevos = (candytemp-1)//(self.candyreq-1)
        diff = ((currevos+1) * (self.candyreq-1) + 1) - candytemp
        if diff != 0 and poketemp - diff >= currevos + 1:
            poketemp -= diff
            candytemp += diff
        # The increments candies and decrements Pokemon by the evolution req
        while poketemp-(self.candyreq-1) >= (candytemp+10)//(self.candyreq-1):
            poketemp -= self.candyreq-1
            candytemp += self.candyreq-1
        # After that, we are left with the exact number of candies to evolve
        # the max possible amount of Pokemon.
        # However many fewer Pokemon we have is the number to transfer
        return (
            min((candytemp-1)//(self.candyreq-1), poketemp),
            self.number-poketemp
            )

    def __str__(self):
        return self.name + " " + str(self.number) + " " + str(self.candy)

def lucky_egg(pokemonlist):
    """
    Tell how many more evolutions are needed to completely use up a Lucky Egg

    Args:
        pokemonlist (list of Species): List of all Species being evolved
    """
    required = 60
    total = 0
    for pokemon in pokemonlist:
        temp = pokemon.calculate_max_evos()
        total += temp[0]
        if total == 1:
            print(pokemon.name + ":\n\tTransfer " + str(temp[1]) +
                  " for a total of " + str(temp[0]) + " evolution.")
        else:
            print(pokemon.name + ":\n\tTransfer " + str(temp[1]) +
                  " for a total of " + str(temp[0]) + " evolutions.")
    if total >= required:
        print("No more Pokemon needed! Get to evolving!")
    else:
        print("You need " + str(required - total) + " more evolutions.")

def main():
    """
    Ask the user for information on their Pokemon and then tell them info

    Loops asking for info until the user gives a blank line.
    After that, tells the user how many Pokemon they can evolve
    and how many more are needed for a "full" lucky egg.
    """
    pokemon = []
    while True:
        name = input("Pokemon name? (blank to end) ")
        if name.strip() == "":
            break
        number = int(input("Currently owned number of " + name + ": "))
        candies = int(input("Number of " + name + " candies owned: "))
        candyreq = int(input("Candies required to evolve one " + name + ": "))
        pokemon.append(Species(name, number, candies, candyreq))
    lucky_egg(pokemon)

main()
