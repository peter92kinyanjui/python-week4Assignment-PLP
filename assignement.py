# This script reads a file, modifies its content, and writes the modified content to a new file.  
def modify_file(input_filename, output_filename):
    try:
        # Step 1: Open the input file for reading
        with open(input_filename, "r") as file:
            content = file.read()  # Read the entire content of the file
            print(f"This is the original content of:{input_filename} \n{content}:")

        # Step 2: Modify the content (for example, convert it to uppercase)
        modified_content = content.upper()  # Example modification

        # Step 3: Open the output file for writing the modified content
        with open(output_filename, "w") as file:
            file.write(modified_content)  # Write the modified content to the new file
            print(f"\nThis is the modified content: \n{modified_content}:")

        print(f"\nThis modified content is saved in {output_filename}.")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
   

# Example usage of the function
modify_file("input.txt", "output.txt")
