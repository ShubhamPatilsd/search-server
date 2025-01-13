import os
import fastapi

def find_files_in_downloads():
    downloads_path = os.path.expanduser('~/Downloads')
    files = []

    for root, dirs, filenames in os.walk(downloads_path):
        for filename in filenames:
            files.append(os.path.join(root, filename))

    return files

if __name__ == "__main__":
    files = find_files_in_downloads()
    for file in files:
        print(file)