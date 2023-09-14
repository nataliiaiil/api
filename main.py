from classes import *
import csv

apple = Fruit("Apple", "Medium", "Sweet and sour")
pear = Fruit("Pear", "Medium", "Sweet")
lemon = Fruit("Lemon", "Medium", "Sour")
watermelon = Fruit("Watermelon", "Grande", "Sweet")
kiwi = Fruit("Kiwi", "Small", "Sour")

fruits_list = [apple, pear, lemon, watermelon, kiwi]

write_list(fruits_list, "fruits_original.csv")
kiwi.change_taste()
write_list(fruits_list, "fruits_updated.csv")

with open("fruits_original.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    
#fw = open("Fruits.txt", "w+")


#pear.fruit_description()
#pear.change_taste()
#pear.fruit_description()