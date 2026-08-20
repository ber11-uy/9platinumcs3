# Annex A
# Computational Thinking Exercise: "Smart School Canteen Queue"

**Section:** 9-Platinum  
**Name:** Amber Gail C. Uy  
**Date:** August 21, 2026  

## Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

- Some students take too long to decide what to order.
- The cashier has to manually calculate totals and give change.
- There is no system to track which food items are running out.

Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

---

## Step 1: Identify the Big Problem

**Main Problem:**

The PSHS school canteen has a slow and crowded lunch process because students take time to decide what to order, payments are calculated manually, and there is no system for tracking food items that are running out.

---

## Step 2: Identify Three to Four Sub-Problems

Please list possible sub-problems:

1. Students take too long to decide what to order, which makes the line move slowly.

2. The cashier has to manually calculate the total price and change, which takes extra time and may cause mistakes.

3. There is no system for checking the food inventory, so staff may not know when an item is running low or unavailable.

4. Many students line up at the same time during lunch, making the canteen crowded and difficult to manage.

---

## Step 3: Define Computational Thinking Approaches

| **Sub-Problem** | **CT Skill** | **Example Solution** |
|---|---|---|
| Students take too long to decide what to order. | Pattern Recognition | Identify the food items that students commonly buy and organize the menu so these items are easier to find. |
| The cashier has to manually calculate the total price and change. | Algorithm Design | Create steps that add the prices of selected items and calculate the correct change. |
| There is no system for checking the food inventory. | Abstraction | Focus on important information such as the food name and quantity available. |
| Many students line up at the same time during lunch. | Decomposition | Break the canteen process into smaller steps such as choosing food, ordering, paying, receiving the food, and leaving the queue. |

---

## Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem

### Selected Sub-Problem

There is no system for checking the food inventory, so staff may not know when an item is running low or unavailable.

### Pseudocode

START

Display the list of food items and their quantities

Ask the staff to select a food item

Check the quantity of the selected food item

IF quantity = 0 THEN
    Display "Item is unavailable"
ELSE IF quantity <= 5 THEN
    Display "Item is running low"
    Display the remaining quantity
ELSE
    Display "Item is available"
    Display the remaining quantity
END IF

END

### Explanation

This algorithm helps the canteen staff check how much food is still available. It tells them if an item is unavailable, running low, or still available. This can help the staff know when they need to prepare or restock more food.

### Reflection

Decomposition helps with the canteen problem because it breaks one large problem into smaller and more manageable parts. Instead of trying to solve the whole canteen problem at once, the ordering, payment, inventory, and queue problems can be handled separately.

The CT skills I used were decomposition, pattern recognition, abstraction, and algorithm design. Pattern recognition can help identify commonly ordered food, abstraction helps focus on important inventory information, and algorithm design gives clear steps for checking the quantity of food available. These CT skills can help make the canteen process faster and more organized.
