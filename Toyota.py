class Toyota:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def start_engine(self):
        return f"The {self.color} {self.brand} engine has started."

    def stop_engine(self):
        return f"The {self.year} Toyota {self.model} engine has stopped."
# Example usage:

toyota_camry = Toyota(color="red", brand="Toyota")

print(toyota_camry.start_engine())
print(toyota_camry.stop_engine())






