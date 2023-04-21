#this script grouping files from directory by their names and extensions:
#example
#input: file1.csv, file1.pdf, file2.csv, file2.pdf
#output(2 main folders):
# filenames/file1/file1.pdf, file1.csv  |  filenames/file2/file2.pdf, file2.csv
# extensions/csv/file1.csv, file2.csv  |  extensions/pdf/file1.pdf, file2.pdf 

import os 
import shutil

dir = "files" #input dir
filename_folder = "filenames"  #output dir for filenames 
extension_folder = "extensions"#output dir for extensions

files = os.listdir(dir)
#print(files)

#by filenames
for file in files:
    file_not_extension = file.rsplit(".",1)[0]
    if not (os.path.exists(f"{filename_folder}\\{file_not_extension}")):
        if not (os.path.exists(filename_folder)):
            os.makedirs(filename_folder)
        os.makedirs(f"{filename_folder}\\{file_not_extension}")
    shutil.copy(f"{dir}\\{file}", f"{filename_folder}\\{file_not_extension}\\{file}")
  
#by extensions  
for file in files:
    file_not_extension = file.rsplit(".",1)[1]
    if not (os.path.exists(f"{extension_folder}\\{file_not_extension}")):
        if not (os.path.exists(extension_folder)):
            os.makedirs(extension_folder)
        os.makedirs(f"{extension_folder}\\{file_not_extension}")
    shutil.copy(f"{dir}\\{file}", f"{extension_folder}\\{file_not_extension}\\{file}")