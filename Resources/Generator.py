import names


class Generator:

    def __init__(self):
        # list of elements that can be accessible from class once function will fill them
        self.list = []

    def generate_names(self, amount):
        amount = int(amount)
        for i in range(amount):
            self.list.append(names.get_full_name())
        return self.list

