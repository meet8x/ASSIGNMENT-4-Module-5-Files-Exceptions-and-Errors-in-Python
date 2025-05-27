try:
    with open("C:/Users/ASUS/Documents/Pylearning/assignment 4/sample.txt", 'r') as file:
       print("Reading file content:")
       readf1 = file.readlines()
       line = 1 
       for i in readf1:
          print("Line",line,":",i)
          line += 1
          
except FileNotFoundError:
    print("Error: The File 'sample.txt' was not found")


