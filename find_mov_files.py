import os
import sys
import subprocess

# Use the current directory if no argument is passed, otherwise use the provided argument
root_dir = sys.argv[1] if len(sys.argv) > 1 else "."

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
                # Write the list of mov files to list.txt
                with open(list_file_path, 'w') as list_file:
                    list_file.write("\n".join(mov_files))
                print(f"List written to: {list_file_path}")

                # Run the first ffmpeg command to merge the mov files into merged.mov
                merged_mov_path = os.path.join(dirpath, "merged.mov")
                ffmpeg_concat_command = ['ffmpeg', '-f', 'concat', '-safe', '0', '-i', list_file_path, '-c', 'copy', merged_mov_path]
                
                # Execute the concat ffmpeg command
                result_concat = subprocess.run(ffmpeg_concat_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                if result_concat.returncode == 0:
                    print(f"Merged MOV file created: {merged_mov_path}")

                    # Run the second ffmpeg command to convert merged.mov to merged.mp4
                    merged_mp4_path = os.path.join(dirpath, "merged.mp4")
                    ffmpeg_convert_command = ['ffmpeg', '-i', merged_mov_path, '-vcodec', 'h264', '-acodec', 'aac', merged_mp4_path]
                    
                    # Execute the ffmpeg command for conversion
                    result_convert = subprocess.run(ffmpeg_convert_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    
                    if result_convert.returncode == 0:
                        print(f"Converted MP4 file created: {merged_mp4_path}")
                    else:
                        print(f"FFmpeg conversion error: {result_convert.stderr.decode('utf-8')}")
                else:
                    print(f"FFmpeg concat error: {result_concat.stderr.decode('utf-8')}")

            except Exception as e:
                print(f"Error writing to {list_file_path}: {e}")
                