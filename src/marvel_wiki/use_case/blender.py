class Blender:
    TRANSFORMATION_MAP = {
        "Red Tree Frog": "mush",
        "apples": "apple juice",
        "iPhone": "toxic waste",
        "Galaxy Nexus": "toxic waste",
    }

    def __init__(self):
        self.thing = None
        self.result = None

    def add(self, thing):
        self.thing = thing

    def switch_on(self):
        self.result = self.TRANSFORMATION_MAP.get(self.thing, "DIRT")
