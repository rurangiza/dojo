"""
Coffee Machine
"""
from helpers import *
from tabulate import tabulate
from typing import List


class CoffeeMachine():
    def __init__(self):
        self.options: dict = {
            "espresso": {"water": 25, "milk": 100, "coffee": 80, "money": 2.5},
            "latte": {"water": 50, "milk": 150, "coffee": 100, "money": 4.},
            "cappuccino": {"water": 50, "milk": 200, "coffee": 100, "money": 6.5}
        }
        self.ingredients = {
            "water": 500,
            "milk": 500,
            "coffee": 500
        }
        self.__money: float = 0.

    def show_options(self):
        items: List[str] = list(self.options.keys())
        print(tabulate(
            [[item, self.options[item]["money"]] for item in items],
            headers=["drink", "price"]
        ))

    def has_ingredients(self, choice) -> bool:
        """
        Check if there is enough ingredients for chosen drink
        """
        for ingredient, quantity in self.options[choice].items():
            if ingredient == "money":
                continue
            if self.ingredients[ingredient] < quantity:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True

    def buy(self, choice: str, coins: float) -> str:
        """
        Server the drink if enough funds and ingredients
        """
        # is there enough money to buy [choice]
        if coins < self.options[choice]["money"]:
            return f"Sorry the inserted money is not enough for a {choice}"

        # pay
        self.__money += self.options[choice]["money"]
        self.ingredients["water"] -= self.options[choice]["water"]
        self.ingredients["milk"] -= self.options[choice]["milk"]
        self.ingredients["coffee"] -= self.options[choice]["coffee"]

        change: float = coins - self.options[choice]["money"]

        print(f"Enjoy your {choice} (change: {change})")


    def report(self) -> None:
        """"
        Show gains and remaining ingredients
        """
        arr = [
            ["Water", f"{self.ingredients['water']}ml"],
            ["Milk", f"{self.ingredients['milk']}ml"],
            ["Coffee", f"{self.ingredients['coffee']}g"],
            ["Money", f"${self.__money:.1f}"]
        ]
        print(tabulate(arr, headers=["ressource", "quantity"]))

    def refill(self) -> None:
        self.ingredients["water"] = 500
        self.ingredients["milk"] = 500
        self.ingredients["coffee"] = 500


def main():
    machine = CoffeeMachine()
    while (choice := prompt_str("What would you like? (espresso/latte/cappuccino): ")) != "off":
        if choice in machine.options:
            if not machine.has_ingredients(choice):
                continue
            price: float = machine.options[choice]["money"]
            coins: float = prompt_int(f"Please insert ${price}: ")
            machine.buy(choice, coins)
        else:
            match choice:
                case "report":
                    machine.report()
                case "refill":
                    machine.refill()
                case "menu":
                    machine.show_options()
                case _:
                    print("Please enter a valid choice")


if __name__ == "__main__":
    main()