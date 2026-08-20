# Name: Amber Gail C. Uy
# Grade & Section: 9-Platinum
# Date: August 21, 2026
# Program: Chinese Zodiac Sign

# List of the 12 Chinese Zodiac signs in their traditional order
zodiac_List = [
    'Rat (鼠 / Shǔ)',
    'Ox (牛 / Niú)',
    'Tiger (虎 / Hǔ)',
    'Rabbit (兔 / Tù)',
    'Dragon (龙 / Lóng)',
    'Snake (蛇 / Shé)',
    'Horse (马 / Mǎ)',
    'Goat (羊 / Yáng)',
    'Monkey (猴 / Hóu)',
    'Rooster (鸡 / Jī)',
    'Dog (狗 / Gǒu)',
    'Pig (猪 / Zhū)'
]


# This function asks the user to enter their birth year
def year():
    # Get the birth year and convert it into an integer
    x = int(input("Enter your birth year: "))
    
    # Return the birth year
    return x


# This function determines the Chinese Zodiac sign
# based on the user's birth year
def get_zodiac(x, y):
    # Calculate the position of the Zodiac sign
    # using 1900 as the starting year for Rat
    year = (x - 1900) % 12
    
    # Get the Zodiac sign from the list
    zodiac = y[year]
    
    # Return the corresponding Zodiac sign
    return zodiac


# Call the year() function to get the user's birth year
x = year()


# Check if the birth year is 1900 or later
if x >= 1900:
    # Determine the user's Chinese Zodiac sign
    animal = get_zodiac(x, zodiac_List)
    
    # Display the user's Chinese Zodiac sign
    print("Your Chinese Zodiac Sign is: " + animal)

else:
    # Display an error message if the year is earlier than 1900
    print("Invalid Year, it should not be earlier than 1900.")