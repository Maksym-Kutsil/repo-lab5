class Fish:
    def __init__(self, name, age, species, size, preferred_food, is_aggressive, needed_space):
        self.name = name
        self.age = age
        self.species = species
        self.size = size
        self.preferred_food = preferred_food
        self.is_aggressive = is_aggressive
        self.needed_space = needed_space

    def __str__(self):
        return f"{self.name}: {self.size} cubic meters"


class Aquarium:
    def __init__(self, total_volume):
        self.total_volume = total_volume
        self.free_space = total_volume
        self.fish_list = []

    def add_fish(self, fish):
        if self.free_space >= fish.needed_space and len(self.fish_list) < 3:
            self.fish_list.append(fish)
            self.free_space -= fish.needed_space
            return True
        else:
            return False

    def get_top_three_largest_fish(self):
        sorted_fish = sorted(self.fish_list, key=lambda x: x.size, reverse=True)
        return sorted_fish[:3]


def main():
    aquarium1 = Aquarium(50)
    aquarium2 = Aquarium(30)

    fish1 = Fish("Nemo", 2, "Clownfish", 0.1, "Plankton", False, 0.5)
    fish2 = Fish("Sharky", 5, "Great White Shark", 4.0, "Other Fish", False, 3.0)
    fish3 = Fish("Dory", 3, "Blue Tang", 0.15, "Algae", False, 0.6)
    fish4 = Fish("Goldie", 1, "Goldfish", 0.05, "Fish Flakes", True, 0.2)
    fish5 = Fish("Angry", 4, "Piranha", 0.3, "Small Fish", True, 1.0)
    fish6 = Fish("Speedy", 2, "Guppy", 0.02, "Fish Flakes", True, 0.1)
    fish7 = Fish("Fluffy", 3, "Angelfish", 0.3, "Worms", False, 0.5)

    aquarium1.add_fish(fish1)
    aquarium1.add_fish(fish2)
    aquarium1.add_fish(fish3)

    aquarium2.add_fish(fish4)
    aquarium2.add_fish(fish5)
    aquarium2.add_fish(fish6)
    aquarium2.add_fish(fish7)

    print("\nTop 3 largest fish in Aquarium 1:")
    top_three_aquarium1 = aquarium1.get_top_three_largest_fish()
    for fish in top_three_aquarium1:
        print(fish)

    print("\nTop 3 largest fish in Aquarium 2:")
    top_three_aquarium2 = aquarium2.get_top_three_largest_fish()
    for fish in top_three_aquarium2:
        print(fish)


if __name__ == "__main__":
    main()
