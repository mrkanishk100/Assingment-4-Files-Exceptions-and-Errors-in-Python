a = input("Enter text to write to the file: ")           # Taking user input and write it to text file

with open("output.txt", "w") as file:                    # Creating and Writing content in text file
    file.write(a + "\n")

print("Data successfully written to output.txt.\n")       

b = input("Enter additional text to append: ")           # Taking user input to Add additional data to same file

with open("output.txt", "a") as file:                    # Adding additional data to same text file
    file.write(b + "\n")

print("Data sucessfully appended ")
print("\nFinal content of output.txt:\n")                

with open("output.txt", "r") as file:                    # Read and display the final data of the file
    for line in file:
        print(line.strip())
