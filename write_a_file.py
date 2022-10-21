text = "Yooooo\nPython is cool\n🐍\n"  
text2 = "I'm on hour 3 of 12 for this python tutorial 🤕" 

with open("test.txt", "w") as file: # note this overwrites the content in test.txt
  file.write(text)

# to append to existing content use "a" as second argument
with open("test.txt", "a") as file:
  file.write(text2)