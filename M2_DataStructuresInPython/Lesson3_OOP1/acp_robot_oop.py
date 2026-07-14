# Base Robot class
class Robot:
    """A general-purpose robot."""
    
    def __init__(self, name: str, model: str, purpose: str):
        self.name = name                # public attribute
        self.model = model
        self.purpose = purpose
        self.__battery_level = 100      # private attribute (encapsulation)
    
    # Getter for battery level
    def get_battery(self) -> int:
        return self.__battery_level
    
    # Setter for battery level (with validation)
    def set_battery(self, level: int) -> None:
        if 0 <= level <= 100:
            self.__battery_level = level
        else:
            print("Battery level must be between 0 and 100.")
    
    # Core method – introduces the robot
    def introduce(self) -> None:
        print(f"Hello! I am {self.name}, model {self.model}.")
        print(f"My purpose: {self.purpose}")
        print(f"Battery level: {self.__battery_level}%")
    
    # Perform a generic task
    def perform_task(self) -> None:
        print(f"{self.name} is performing a generic task.")
        self.__battery_level -= 10
        if self.__battery_level < 0:
            self.__battery_level = 0
    
    # Charge the robot
    def charge(self, amount: int) -> None:
        new_level = self.__battery_level + amount
        self.set_battery(new_level)


# Child class: ServiceRobot (inherits from Robot)
class ServiceRobot(Robot):
    """A robot specialised in providing services."""
    
    def __init__(self, name: str, model: str, purpose: str, service_type: str):
        super().__init__(name, model, purpose)
        self.service_type = service_type
    
    # Override introduce() to include service info
    def introduce(self) -> None:
        super().introduce()  # call parent's method
        print(f"I specialise in {self.service_type} services.")
    
    # Override perform_task() for service-specific behaviour
    def perform_task(self) -> None:
        print(f"{self.name} is providing {self.service_type} service.")
        # Service consumes less battery
        current = self.get_battery()
        self.set_battery(current - 5)


# Child class: CombatRobot (inherits from Robot)
class CombatRobot(Robot):
    """A robot designed for combat and security."""
    
    def __init__(self, name: str, model: str, purpose: str, weapon: str):
        super().__init__(name, model, purpose)
        self.weapon = weapon
    
    # Override introduce()
    def introduce(self) -> None:
        super().introduce()
        print(f"I am armed with {self.weapon}.")
    
    # Override perform_task()
    def perform_task(self) -> None:
        print(f"{self.name} is engaging targets with {self.weapon}.")
        current = self.get_battery()
        self.set_battery(current - 20)  # combat consumes more energy


# --------------------- Demonstration (Polymorphism) ---------------------
if __name__ == "__main__":
    # Create a list of different robots (polymorphic collection)
    robots = [
        Robot("Alpha", "R-100", "General assistance"),
        ServiceRobot("Beta", "S-200", "Customer support", "cleaning"),
        CombatRobot("Gamma", "C-300", "Security patrol", "laser cannon")
    ]
    
    print("===== ROBOT INTRODUCTIONS =====")
    for bot in robots:
        bot.introduce()          # polymorphic call – each uses its own version
        print("-" * 40)
    
    # Show task execution (polymorphism again)
    print("\n===== PERFORMING TASKS =====")
    for bot in robots:
        bot.perform_task()
        print(f"Battery after task: {bot.get_battery()}%")
        print("-" * 40)