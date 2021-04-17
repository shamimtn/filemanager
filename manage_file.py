import os
import glob


os.chdir('E:\project')
list_files=glob.glob('*')
my_set=set()
my_list=[]
for each_file in list_files:
    extention=each_file.split('.')[-1:]
    for ext in extention:
        my_set.add(ext)

    
    

def create_folder():
    for ext in my_set:
        os.mkdir(ext+'_file')


def move_file():
    for each_file in list_files:
        exstentions=each_file.split('.')[-1:]
    for ex in extention:
        os.rename(each_file,ex+"_file/"+each_file)

        


create_folder()
move_file()