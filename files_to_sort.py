import os
import shutil


def main():
    os.chdir('FilesToSort')
    file_types = []
    for file in os.listdir('.'):
        file_name, file_extension = os.path.splitext(file)
        new_folder = file_extension.replace(".", "")
        if new_folder not in file_types:
            file_types.append(new_folder)
    print(file_types)

    for extension in file_types:
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

    for file in os.listdir('.'):
        file_name, file_extension = os.path.splitext(file)
        new_folder = file_extension.replace(".", "")
        shutil.move(file, new_folder)

main()
