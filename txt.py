import os

# Set the directory path containing .png files
directory_path = r'C:\Users\User\Desktop\test'

# Replace backslashes with forward slashes in the path
# if the Path is from Windows Explorer
directory_path = directory_path.replace(r'\\', '/')

# Get a list of all .png files in the directory
png_files = [f for f in os.listdir(directory_path) if f.endswith('.png')]

# Loop through each .png file and create a new text file
for png_file in png_files:
    txt_file_path = os.path.join(directory_path, os.path.splitext(png_file)[0] + '.txt')
    with open(txt_file_path, 'w') as txt_file:
	# Replace this Text with your Tags that work for all images in this directory
        txt_file.write(f'This is a text file associated with the image {png_file}')