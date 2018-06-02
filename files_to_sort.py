import os
import shutil


def main():

    os.chdir('FilesToSort')
    make_folders()

    for file in os.listdir('.'):
        sort_files(file)


def sort_files(file):
    if file.endswith(".xlsx"):
        shutil.move(file, 'xlsx')
    elif file.endswith(".xls"):
        shutil.move(file, 'xls')
    elif file.endswith(".txt"):
        shutil.move(file, 'txt')
    elif file.endswith(".png"):
        shutil.move(file, 'png')
    elif file.endswith(".jpg"):
        shutil.move(file, 'jpg')
    elif file.endswith(".gif"):
        shutil.move(file, 'gif')
    elif file.endswith(".docx"):
        shutil.move(file, 'docx')
    elif file.endswith(".doc"):
        shutil.move(file, 'doc')


def make_folders():
    try:
        os.mkdir('xlsx')
    except FileExistsError:
        pass
    try:
        os.mkdir('xls')
    except FileExistsError:
        pass
    try:
        os.mkdir('txt')
    except FileExistsError:
        pass
    try:
        os.mkdir('png')
    except FileExistsError:
        pass
    try:
        os.mkdir('jpg')
    except FileExistsError:
        pass
    try:
        os.mkdir('gif')
    except FileExistsError:
        pass
    try:
        os.mkdir('docx')
    except FileExistsError:
        pass
    try:
        os.mkdir('doc')
    except FileExistsError:
        pass


main()
