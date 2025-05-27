text1 = input("Enter text to write to the file:")

with open("C:/Users/ASUS/Documents/Pylearning/assignment 4/samplefile.txt", 'w') as file:
       file.write(text1)
       file.close()
print("Data Successfully written to output.txt")

text2 = input("Enter additional text to append:")
with open("C:/Users/ASUS/Documents/Pylearning/assignment 4/samplefile.txt", 'a') as file:
       file.write("\n" + text2)
       file.close()
print("Data Successfully Appended")


with open("C:/Users/ASUS/Documents/Pylearning/assignment 4/samplefile.txt", 'r') as file:
       file_contetnt = file.read()
print(file_contetnt)