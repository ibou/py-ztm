import sys, os
from PIL import Image


# list all image files in a directory Pokedex
def list_images():
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image-playground/Pokedex')
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            print(filename)
    return directory

# convert all images in a directory from JPG to PNG
def convert_images(from_directory, to_directory):
    for filename in os.listdir(from_directory):
        if filename.endswith('.jpg'):
            img = Image.open(f'{from_directory}/{filename}')
            img.save(f'{to_directory}/{filename[:-4]}.png', 'png')
            print(f'{filename} converted to PNG')
            
def main():
    from_directory = list_images()
    to_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image-playground/new')
    print(to_directory)
    # create directory to_directory if it does not exist
    if not os.path.exists(to_directory):
        os.makedirs(to_directory)
    
    convert_images(from_directory, to_directory)
    

if __name__ == '__main__':
    main()
    