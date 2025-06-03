Word=["Donkey","bad"]


with open("file.tx")as f:
    content=f.read()


newcontent=content.replace("Donkey","#####")
with open("file.tx")as f:
    f.write(newcontent)  


    print("Updated")  