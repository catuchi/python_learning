# copyfile() = copies content of a file
# copy()     = copyfile() + permissions + destination can be a directory
# copy2()    = copy() + metadata (file's creation and modification times)

import shutil

shutil.copyfile("test.txt","copy.txt") # copy.txt is automatically created

# same arguments for copy and copy2
# shutil.copy("test.txt","copy.txt") # copy.txt is automatically created
# shutil.copy2("test.txt","copy.txt") # copy.txt is automatically created
