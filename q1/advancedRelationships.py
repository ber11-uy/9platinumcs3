class ResonancePoint:
    def __init__(self, timestamp, mood, intensity):
        self.timestamp = timestamp
        self.mood = mood
        self.intensity = intensity

    def displayPoint(self):
        print(
            self.timestamp,
            "| Mood:", self.mood,
            "| Intensity:", self.intensity
        )


class Melodyssey:
    def __init__(self, startingMood, endingMood, energyLevel, duration):
        self.startingMood = startingMood
        self.endingMood = endingMood
        self.energyLevel = energyLevel
        self.__duration = duration

        # Composition: Melodyssey keeps its own ResonancePoints
        self.__resonancePoints = []

    def changeMood(self, newMood):
        self.endingMood = newMood

    def increaseEnergy(self, amount):
        self.energyLevel += amount

        # Keeps the energy level within the 1-10 range
        if self.energyLevel > 10:
            self.energyLevel = 10

        if self.energyLevel < 1:
            self.energyLevel = 1

    def addResonancePoint(self, timestamp, mood, intensity):
        # Creates a ResonancePoint as part of the Melodyssey
        point = ResonancePoint(timestamp, mood, intensity)
        self.__resonancePoints.append(point)

    def displayJourney(self):
        print("Starting Mood:", self.startingMood)
        print("Ending Mood:", self.endingMood)
        print("Energy Level:", self.energyLevel)
        print("Duration:", self.getDuration(), "minutes")

    def displayResonanceMap(self):
        print("Resonance Points:")

        for point in self.__resonancePoints:
            point.displayPoint()

    def getDuration(self):
        return self.__duration

    def getResonancePointCount(self):
        return len(self.__resonancePoints)


# EvolvingMelodyssey inherits from Melodyssey
class EvolvingMelodyssey(Melodyssey):
    def __init__(
        self,
        startingMood,
        endingMood,
        energyLevel,
        duration,
        evolutionStyle
    ):
        # Reuses the constructor of Melodyssey
        super().__init__(
            startingMood,
            endingMood,
            energyLevel,
            duration
        )

        self.evolutionStyle = evolutionStyle

    def displayEvolution(self):
        self.displayJourney()
        print("Evolution Style:", self.evolutionStyle)


# Test 1: Inheritance
print("=== TEST 1: INHERITANCE ===")

melody1 = EvolvingMelodyssey(
    "Calm",
    "Powerful",
    6,
    4.5,
    "Gradual Build-Up"
)

print("EvolvingMelodyssey object:")
melody1.displayEvolution()

print()
print("Using inherited method increaseEnergy(2)...")
melody1.increaseEnergy(2)

print("Energy Level after increaseEnergy(2):", melody1.energyLevel)


# Test 2: Composition
print()
print("=== TEST 2: COMPOSITION ===")

melody1.addResonancePoint("00:45", "Calm", 3)
melody1.addResonancePoint("02:30", "Hopeful", 7)
melody1.addResonancePoint("04:10", "Powerful", 10)

print("Melodyssey contains ResonancePoints:")
melody1.displayResonanceMap()

print()
print("Total ResonancePoints:", melody1.getResonancePointCount())