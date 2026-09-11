class Melodyssey:
    def __init__(self, startingMood, endingMood, energyLevel, duration):
        self.startingMood = startingMood
        self.endingMood = endingMood
        self.energyLevel = energyLevel
        self.__duration = duration
        self.resonancePoints = []

    def changeMood(self, newMood):
        self.endingMood = newMood

    def increaseEnergy(self, amount):
        self.energyLevel += amount

        if self.energyLevel > 10:
            self.energyLevel = 10

        if self.energyLevel < 1:
            self.energyLevel = 1

    def addResonancePoint(self, point):
        self.resonancePoints.append(point)

    def displayJourney(self):
        print("Starting Mood:", self.startingMood)
        print("Ending Mood:", self.endingMood)
        print("Energy Level:", self.energyLevel)
        print("Duration:", self.getDuration(), "minutes")

    def displayResonanceMap(self):
        print("Resonance Points:")
        for point in self.resonancePoints:
            point.displayPoint()

    def getDuration(self):
        return self.__duration


class ResonancePoint:
    def __init__(self, timestamp, mood, intensity):
        self.timestamp = timestamp
        self.mood = mood
        self.intensity = intensity

    def displayPoint(self):
        print(
            self.timestamp,
            "- Mood:", self.mood,
            "| Intensity:", self.intensity
        )


# Main Melodyssey object
melody = Melodyssey(
    "Calm",
    "Euphoric",
    6,
    4.5
)

# ResonancePoint objects
point1 = ResonancePoint("0:45", "Calm", 3)
point2 = ResonancePoint("2:10", "Tense", 7)
point3 = ResonancePoint("3:50", "Euphoric", 10)


# BEFORE RELATIONSHIP
print("--- BEFORE RELATIONSHIP ---")
print("Melodyssey object created: melody")
melody.displayJourney()

print()
print("ResonancePoint objects created:")
point1.displayPoint()
point2.displayPoint()
point3.displayPoint()


# BUILDING RELATIONSHIP
print()
print("--- BUILDING RELATIONSHIP ---")
print("Adding ResonancePoint objects to melody...")
melody.addResonancePoint(point1)
melody.addResonancePoint(point2)
melody.addResonancePoint(point3)


# AFTER RELATIONSHIP
print()
print("--- AFTER RELATIONSHIP ---")
print("Melodyssey can now access its ResonancePoint objects.")
melody.displayJourney()

print()
melody.displayResonanceMap()