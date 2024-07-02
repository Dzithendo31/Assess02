import os

def add_to_authority(keyword):
    dirz = r'C:\Users\e1005282\Videos\CD-Test'
    for filename in os.listdir(dirz):
        print(filename)

add_to_authority('123')