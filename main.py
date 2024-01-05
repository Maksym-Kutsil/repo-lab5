class Fish:
    def __init__(self, name, age, species, size, preferred_food, is_aggressive, needed_space):
        self.name = name
        self.age = age
        self.species = species
        self.size = size
        self.preferred_food = preferred_food
        self.is_aggressive = is_aggressive
        self.needed_space = needed_space


class Aquarium:
    def __init__(self, total_volume):
        self.total_volume = total_volume
        self.free_space = total_volume
        self.aggressive_fish = []
        self.non_aggressive_fish = []

    def add_fish(self, fish):
        if fish.is_aggressive is True and self.free_space >= fish.needed_space:
            self.aggressive_fish.append(fish)
            self.free_space -= fish.needed_space
        elif fish.is_aggressive is False and self.free_space >= fish.needed_space:
            self.non_aggressive_fish.append(fish)
            self.free_space -= fish.needed_space

    def get_top_three_largest_fish(self):
        self.aggressive_fish.sort(key=lambda x: x.size, reverse=True)
        self.non_aggressive_fish.sort(key=lambda x: x.size, reverse=True)


def main():
    non_agressive_aquarium = Aquarium(4)
    agressive_aquarium = Aquarium(30)

    fish1 = Fish("NemoFish", 2, "Clownfish", 0.1, "Plankton", False, 0.5)
    fish2 = Fish("SharkyFish", 5, "Great White Shark", 4.0, "Other Fish", False, 3.0)
    fish3 = Fish("DoryFish", 3, "Blue Tang", 0.15, "Algae", False, 0.6)
    fish4 = Fish("GoldieFish", 1, "Goldfish", 0.05, "Fish Flakes", True, 0.2)
    fish5 = Fish("AngryFish", 4, "Piranha", 0.3, "Small Fish", True, 1.0)
    fish6 = Fish("SpeedyFish", 2, "Guppy", 0.02, "Fish Flakes", True, 0.1)
    fish7 = Fish("FluffyFish", 3, "Angelfish", 0.3, "Worms", False, 0.5)

    fish_list = (fish1, fish2, fish3, fish4, fish5, fish6, fish7)
    for fish in fish_list:
        if fish.is_aggressive:
            agressive_aquarium.add_fish(fish)
        else:
            non_agressive_aquarium.add_fish(fish)

    non_agressive_aquarium.get_top_three_largest_fish()
    agressive_aquarium.get_top_three_largest_fish()

    print("Fish in non_agressive_aquarium:")
    for fish in non_agressive_aquarium.non_aggressive_fish[:3]:
        print(f"{fish.name}: {fish.size} cubic meters")

    print("\nFish in agressive_aquarium:")
    for fish in agressive_aquarium.aggressive_fish[:3]:
        print(f"{fish.name}: {fish.size} cubic meters")


if __name__ == "__main__":
    main()
