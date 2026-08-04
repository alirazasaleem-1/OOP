class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand 
        self.power_rating = power_rating
        self.turn_on = False 

        def turn_on(self) -> None:
            if turn_on:
                print(f"Microwave ({self.brand}) is already turned on")
            else:
                self.turn_on = True 
                print(f"Microwave ({self.turn_on}) is now turned on.")

        def turn_off(self) -> None:
            if turn_on:
                 self.turned_on = False 
                 print(f"Microwave ({self.brand}) is now turned off.")
            else:
                 print(f"Microwave ({self.turn_on}) is already turned off.")

        def run(self, seconds: int) -> None: 
            if self.turned_on:
                print(f"Running ({self.brand}) for ({seconds})")
            else:
                print(f'A mystical force whispers: "Turn on your microwave first..."')
                    


smeg: Microwave = Microwave() 
