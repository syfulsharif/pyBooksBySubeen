# Taking "all_countries.txt" as input file
# in reading mode
with open("all_countries.txt", "r") as input:
    # Creating "a.txt" as output
    # file in write mode

    with open("a.txt", "w") as output:
        for line in input:
            if line.startswith("A"):
                output.write(line+"\n")
