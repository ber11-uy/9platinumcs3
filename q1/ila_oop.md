# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation

Encapsulation can be used by putting the product's name, price, and stock in one `Product` class. Instead of changing the stock directly, methods like `sell_product()` and `restock_product()` can be used to update it. This keeps the product information together and makes the inventory easier to manage.

### 2. Abstraction

Abstraction can be used by creating simple methods for common store actions, such as selling or restocking a product. The person using the program does not need to know every step that happens inside the method. They only need to use the method to perform the action they want.

### 3. Inheritance

Inheritance can be useful if the store has different kinds of products. For example, `FoodProduct` and `DrinkProduct` can inherit the basic information from a `Product` class while having their own additional details. This avoids having to write the same code again for every type of product.

### 4. Polymorphism

Polymorphism can be used when different types of products need to perform the same action in different ways. For example, both `FoodProduct` and `DrinkProduct` could have a `display_info()` method, but each one could display information differently. This allows the program to use the same method while still handling different types of products.

## Simple Class Representation

```text
              Product
        ┌──────────────────┐
        │ name             │
        │ price            │
        │ quantity         │
        ├──────────────────┤
        │ sell_product()   │
        │ restock_product()│
        │ display_info()   │
        └────────┬─────────┘
                 │
        ┌────────┴─────────┐
        │                  │
   FoodProduct       DrinkProduct
```

## Reflection

Among the four pillars, I think encapsulation would be the most useful for the sari-sari store inventory system. Since the program needs to keep track of things like product prices and stock, putting these details together in a class would make everything more organized. It would also make it easier to update the inventory without accidentally changing the wrong information. As the store adds more products, this would make the program easier to manage.