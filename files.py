#var = input("Write your shit here: ")
#fw = open('directory/file.txt', 'a')
#fw.write(var)
#fw.close()

fa = open("directory/file.txt", "r")
text = fa.read()
fa.close()

print(text)