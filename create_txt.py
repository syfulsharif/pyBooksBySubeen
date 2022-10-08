lines = ["This is first line",
         "This is second line",
         "This is third line"]

with open("file2.txt", "w") as fp:
    for line in fp:
        fp.write(line+"\n")
