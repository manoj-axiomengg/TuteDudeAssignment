with open("output.txt", 'w') as file:
    text = input("Enter  text to write to the file:")
    file.write(text + "\n")
    print("Data successfully written to output.txt")

with open("output.txt", "a") as file:
    text_append = input("Enter additional text to apppend :")
    file.write(text_append + "\n")
    print("Data successfully appended.")

with open("output.txt", "r") as file:
    text_read = file.read()
    print("Final content of output.txt :")
    print(text_read)
    