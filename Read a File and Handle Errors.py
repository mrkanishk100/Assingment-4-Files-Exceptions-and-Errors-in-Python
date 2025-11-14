try:                                                  # Program to read and print the contents of Text File
    with open("sample.txt", "r") as file:             # Opening File in Read Mode
        print("Reading file content:\n")
                                                  
        for index, line in enumerate(file, start=1):  # Read and print each line with line numbers 
            print(f"Line {index}: {line.strip()}")

except FileNotFoundError:                             # In case File Not Found
    print("Error: The file 'sample.txt' was not found.")

