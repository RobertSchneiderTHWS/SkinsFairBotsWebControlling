import importlib
import time

class Loop:
    def __init__(self):
        self.files = ["BuyTrendProductBot", "CustomerJourneyBot", "DeleteCartBot", "RandomSaleProductWithDifferentCurrencyBot", "RandomUserClickingBot"]
        self.modules = []
        for file in self.files:
            self.modules.append(importlib.import_module(file))

    def run(self):
        counter = 0
        exceptions = 0
        while True:
            for module in self.modules:
                counter += 1
                try:
                    module.run()
                except Exception as e:
                    exceptions += 1
                    print(e)
                time.sleep(5)
                print(f"Counter: {counter} \nExceptions: {exceptions}\n")


if __name__ == "__main__":
    loop = Loop()
    loop.run()