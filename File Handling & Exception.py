# File Read & Write with Error Handling

def modify_file_content(content):
    # Example modification: convert all text to uppercase
    return content.upper()

def main():
    filename = input("Enter the name of the file to read: ")

    try:
        # Open the file and read its content
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_file_content(content)

        # Create a new file to write the modified content
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}' successfully.")

    except FileNotFoundError:
        print("Error: The file you entered does not exist.")
    except IOError:
        print("Error: Unable to read the file.")

if __name__ == "__main__":
    main()
