import os
import distutils.dir_util
x = 1 #var for establishing junk folders
root1_path = 'C:\\Users\\Kai\\Desktop\\Root\\Root1'
root2_path = 'C:\\Users\\Kai\\Desktop\\Root\\Root2'
while True:
    os.chdir(root1_path)
    try:
        user_input = input("Enter a folder name or '/break' to end the program: ")
        if user_input == '/break': #ends program with break input
            break
        else:
            os.mkdir(user_input)
            print("Folder named", user_input, "created")
            x = x + 1
            os.chdir(root2_path)
            new_junk = "Junk"+ str(x) #name for newjunk in root2
            os.mkdir(new_junk) 
            dst = os.path.join(root2_path, new_junk) #adds new junk to path
            src = root1_path + '\\Junk'
            distutils.dir_util.copy_tree(src, dst)
    except FileExistsError: 
        print('Folder already exists. Try another name')
