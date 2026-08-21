# Chinese Zodiac Coding Exercise

**Name:** Amber Gail C. Uy  
**Grade & Section:** 9-Platinum 
**Date:** August 21, 2026  

## Requirements

The program must:

1. Ask the user to enter a year of birth using 1900 as the baseline year.
2. Validate that the entered year is not earlier than 1900.
3. If the user enters an invalid year, display an appropriate message and stop the program.
4. Determine the Chinese Zodiac sign based on the year of birth.
5. Use the 12 Chinese Zodiac signs in the required order.
6. Consider only the year of birth.
7. Test and run the program before submitting.

The 12 Chinese Zodiac signs are:

1. Rat (鼠 / Shǔ)
2. Ox (牛 / Niú)
3. Tiger (虎 / Hǔ)
4. Rabbit (兔 / Tù)
5. Dragon (龙 / Lóng)
6. Snake (蛇 / Shé)
7. Horse (马 / Mǎ)
8. Goat (羊 / Yáng)
9. Monkey (猴 / Hóu)
10. Rooster (鸡 / Jī)
11. Dog (狗 / Gǒu)
12. Pig (猪 / Zhū)

## Actual Code

```python
# Name: Amber Gail C. Uy
# Grade & Section: 9-Platinum
# Date: August 21, 2026
# Coding Exercise: Chinese Zodiac Sign

# List of the 12 Chinese Zodiac signs
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


# Ask the user to enter their year of birth
def year():
    x = int(input("Enter your birth year: "))
    return x


# Determine the Chinese Zodiac sign
def get_zodiac(x, y):
    # Calculate the position of the Zodiac sign
    # using 1900 as the baseline year
    index = (x - 1900) % 12

    # Return the corresponding Zodiac sign
    return y[index]


# Get the user's birth year
x = year()


# Validate the user's input
if x < 1900:
    print("Invalid Year, it should not be earlier than 1900.")

else:
    # Determine the user's Chinese Zodiac sign
    animal = get_zodiac(x, zodiac_List)
```

## Program Output and Screenshot
<img width="1525" height="831" alt="Screenshot 2026-08-21 013303" src="https://github.com/user-attachments/assets/05f7b07c-a5ac-4b2a-aa51-d690ec27ab69" />


