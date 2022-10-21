import os
import shutil

path = "./test_text.txt"
path2 = "./empty_folder"
path3 = "./not_empty_folder"

try:
  # os.remove(path2)      # this does not remove empty directories
  # os.rmdir(path2)       # this removes empty directories but not directories with files
  shutil.rmtree(path3)    # this removes a full directory. be careful with this ❗ ❗
  print("deleted")
except FileNotFoundError as e:
  print(e)
except PermissionError as e:
  print(e)
except OSError as e:
  print(e)