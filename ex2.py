class IceCreamMachine:
    all={}
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        res = []
        for l in self.ingredients:
            for m in self.toppings:
                res.append([l, m])
        return res

machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops()) 