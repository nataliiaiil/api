import csv
class Fruit():
    
    def __init__(self, name, size, taste):
        self.name = name
        self.size = size
        self.taste = taste
    
    def fruit_description(self):
        print("Fruit is named " + self.name + ", its size is " + self.size + ", and it tastes " + self.taste)

    def get_taste(self):
        print("The " + self.name + "tastes " + self.taste)

    def change_taste(self):
        changed_taste = input("Enter " + self.name + "'s new taste: ")
        self.taste = changed_taste
        print("New taste of " + self.name + " is " + self.taste)
    
def write_list(list, csvfile):
    with open(csvfile, mode="w+", newline="") as myfile:
        wr = csv.writer(myfile)
        for i in list:
            wr.writerow([i.name, i.size, i.taste])