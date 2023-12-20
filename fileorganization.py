# file handling: navigate, rename, move, copy, remove

import os

print(os.getcwd()) # pwd
os.chdir("/Users/vishnumano/Desktop") # cd
print(os.listdir()) # ls

counter = 1
for file in os.listdir():
    if file[0] == ".":
        continue
    name, ext = os.path.splitext(file)
    print(name)
    print(ext)
    splitted = name.split(" ")
    splitted = [s.strip() for s in splitted]
    new_name = f"{str(counter).zfill(2)}->{splitted[1]}_{splitted[3]}{splitted[4]}->{splitted[0]}{ext}"
    os.rename(file, new_name)
    counter += 1