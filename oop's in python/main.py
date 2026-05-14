class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on = False

    def turn_on(self):
        if self.turned_on:
            print(f"Microwave {self.brand} is already turned on")
        else:
            self.turned_on = True
            print(f"Microwave {self.brand} is now turned on")

    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave {self.brand} is now turned off")
        else:
            
            print(f"Microwave {self.brand} is already turned off")

    def run(self, seconds: int):
        if self.turned_on:
            print(f"Running {self.brand} for {seconds} seconds")
        else:
            print(f"A mystical force whispers: 'Turn on your microwave first...'")

    def __str__(self):
        return f"Power Rating {self.power_rating}"

smeg: Microwave = Microwave('smeg', 'B')
smeg.turn_on()
smeg.turn_on()
smeg.run(56)
smeg.turn_off()
smeg.turn_off()
smeg.run(44)

print(smeg)

'''
Output :

Microwave smeg is now turned on
Microwave smeg is already turned on
Running smeg for 56 seconds
Microwave smeg is now turned off
Microwave smeg is already turned off
A mystical force whispers: 'Turn on your microwave first...'

'''