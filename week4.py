def read_and_modify_file():
    try:
        # Ask the user for the filename
        filename = input("Enter the filename to read: ")

        # Open the file for reading
        with open(filename, "r") as file:
            content = file.read()

        # Modify content (convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content saved to '{new_filename}'")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename.")
    except IOError:
        print("Error: Could not read the file. Check file permissions.")

# Run the function
read_and_modify_file()
