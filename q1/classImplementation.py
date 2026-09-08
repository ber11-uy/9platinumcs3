class Melodyssey:
    def __init__(self, startingMood, endingMood, energyLevel, duration):
        self.startingMood = startingMood
        self.endingMood = endingMood
        self.energyLevel = energyLevel
        self.__duration = duration

    def changeMood(self, newMood):
        self.endingMood = newMood

    def increaseEnergy(self, amount):
        self.energyLevel += amount

        if self.energyLevel > 10:
            self.energyLevel = 10

        if self.energyLevel < 1:
            self.energyLevel = 1

    def displayJourney(self):
        print("Starting Mood:", self.startingMood)
        print("Ending Mood:", self.endingMood)
        print("Energy Level:", self.energyLevel)
        print("Duration:", self.getDuration(), "minutes")

    def getDuration(self):
        return self.__duration


# Object 1
melody1 = Melodyssey(
    "Calm",
    "Hopeful",
    6,
    4.5
)

# Object 2
melody2 = Melodyssey(
    "Mysterious",
    "Joyful",
    4,
    3.25
)


# Initial states
print("--- BEFORE ---")

print("Object 1: melody1")
melody1.displayJourney()

print()

print("Object 2: melody2")
melody2.displayJourney()


# Change only Object 1
print()
print("Performing increaseEnergy(3) on Object 1...")
melody1.increaseEnergy(3)


# Updated states
print()
print("--- AFTER ---")

print("Object 1: melody1")
melody1.displayJourney()

print()

print("Object 2: melody2")
melody2.displayJourney()