import os
import sys


# Use the current directory if no argument is passed, otherwise use the provided argument
root_dir = sys.argv[1] if len(sys.argv) > 1 else "."

print(f"Reading folder: {root_dir}")

# Walk through the directory tree
for dirpath, dirnames, filenames in os.walk(root_dir):
    # Check if the current directory is named "Original Media"
    if os.path.basename(dirpath) == "Original Media":
        # List to hold .mov file entries
        mov_files = []

        # List all .mov files in the "Original Media" directory
        for file in filenames:
            if file.endswith(".mov"):
                # Add each .mov file to the list in the required format
                mov_files.append(f'file "{file}"')

        # Sort the list of .mov files by filename
        mov_files.sort()

        # If any .mov files were found, write them to list.txt in the same directory
        if mov_files:
            list_file_path = os.path.join(dirpath, "list.txt")
            try:
                with open(list_file_path, 'w') as list_file:
                    # Write each formatted .mov file name into list.txt
                    list_file.write("\n".join(mov_files))
                print(f"List written to: {list_file_path}")
            except Exception as e:
                print(f"Error writing to {list_file_path}: {e}")

                