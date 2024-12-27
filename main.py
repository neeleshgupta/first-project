class SimpleClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

# Example usage
if __name__ == "__main__":
    obj = SimpleClass("Pilot")
    print(obj.greet())
    