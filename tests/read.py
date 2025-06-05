import os

def extract_and_combine_python_files(directory, output_file):
    # Ensure the provided path is a directory
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory.")
        return

    # Open the output file in 'w' mode to write
    with open(output_file, 'w') as output_file:
        # Iterate through all files in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            # Check if the current item is a file and ends with ".py"
            if os.path.isfile(file_path) and filename.endswith(".py"):
                print(f"Reading contents of file: {filename}")

                # Open the file and read its contents
                with open(file_path, 'r') as file:
                    file_contents = file.read()

                    # Write the contents to the output file
                    output_file.write(file_contents)
                    output_file.write("\n" + "=" * 50 + "\n")  # Separating lines for better visibility

    print(f"All Python files in {directory} have been combined into {output_file.name}")

if __name__ == "__main__":
    # Replace 'your_directory_path' with the path to your directory containing Python files
    directory_path = './schedulizer'
    
    # Replace 'output_combined_file.py' with the desired output file name
    output_file_path = 'all.py'

    extract_and_combine_python_files(directory_path, output_file_path)

