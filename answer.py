from abc import ABC, abstractmethod
from typing import List
class Superhero(ABC):
    def __init__(self, name: str, secret_identity: str, power_level: init):
        self.name = name
        self.secret_identity = secret_identity
        self.power_level = power_level
        self.abilities = []
    
    @abstractmethod
    def move(self):
        """Abstract method for movement - must be implemented by child classes"""
        pass
    
    @abstractmethod
    def use_power(self):
        """Abstract method for using powers - must be implemented by child classes"""
        pass
    
    def display_info(self):
        """Display hero information"""
        return f"{self.name} (Power Level: {self.power_level})"

class FlyingHero(Superhero):
    def __init__(self, name: str, secret_identity: str, power_level: int, flight_speed: int):
        super().__init__(name, secret_identity, power_level)
        self.flight_speed = flight_speed
        self.abilities = ["Flight", "Wind Control"]
    
    def move(self):
        return f"{self.name} is flying at {self.flight_speed} mph!"
    
    def use_power(self):
        return f"{self.name} creates a powerful whirlwind!"

class TechHero(Superhero):
    def __init__(self, name: str, secret_identity: str, power_level: int, gadgets: List[str]):
        super().__init__(name, secret_identity, power_level)
        self.gadgets = gadgets
        self.abilities = ["Tech Expertise", "Gadget Mastery"]
    
    def move(self):
        return f"{self.name} moves with enhanced tech-suit propulsion!"
    
    def use_power(self):
        return f"{self.name} deploys {', '.join(self.gadgets)}!"

class Speedster(Superhero):
    def __init__(self, name: str, secret_identity: str, power_level: int, max_speed: int):
        super().__init__(name, secret_identity, power_level)
        self.max_speed = max_speed
        self.abilities = ["Super Speed", "Speed Force"]
    
    def move(self):
        return f"{self.name} zooms past at incredible speed!"
    
    def use_power(self):
        return f"{self.name} creates a speed vortex!"

# Example usage
def main():
    # Create different types of heroes
    iron_man = TechHero("Iron Man", "Tony Stark", 9, ["Repulsor", "Missiles"])
    flash = Speedster("The Flash", "Barry Allen", 10, 186282)
    superman = FlyingHero("Superman", "Clark Kent", 11, 770)
    
    # Store heroes in a list
    heroes = [iron_man, flash, superman]
    
    # Demonstrate polymorphism
    print("=== Hero Showcase ===")
    for hero in heroes:
        print(f"\n{hero.display_info()}")
        print(f"Abilities: {', '.join(hero.abilities)}")
        print(hero.move())
        print(hero.use_power())

if __name__ == "__main__":
    main()