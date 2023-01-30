class Money_manager:
    def __init__(self):
        self.file_name = "money_flow.txt"
        with open(self.file_name, "a+") as f:
            f.seek(0)
            self.money_flow = f.readlines()

    def show_balance(self):
        balance = 0
        for line in self.money_flow:
            line = line.strip().split("|")
            for item in line:
                item = item.strip().split(" - ")
                if len(item) != 2:
                    continue
                if item[0].strip().isdigit():
                    continue
                if item[1].strip().isdigit():
                    balance += int(item[1].strip()) if item[0].strip() == "Income" else -int(item[1].strip())
        print("-------------")
        for line in self.money_flow:
            line = line.strip().split("|")
            for item in line:
                item = item.strip().split(" - ")
                if len(item) != 2:
                    continue
                print("{} {}".format(item[0].strip(), "+" + item[1].strip() if item[0].strip() == "Income" else "-" + item[1].strip()))
        print("\n------------\nThe balance is {} GEL".format(balance))

    def add_revenue_cost(self, revenue_cost):
        with open(self.file_name, "a") as f:
            f.write(revenue_cost + "\n")
        with open(self.file_name, "r") as f:
            self.money_flow = f.readlines()

    def remove_revenue_cost(self, revenue_cost):
        with open(self.file_name, "r") as f:
            lines = f.readlines()
        with open(self.file_name, "w") as f:
            for line in lines:
                if line.strip() != revenue_cost:
                    f.write(line)
        with open(self.file_name, "r") as f:
            self.money_flow = f.readlines()