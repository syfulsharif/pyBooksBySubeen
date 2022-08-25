saarc = ["bangladesh", "afghanistan", "bhutan",
         "nepal", "india", "pakistan", "sri Lanka"]

country = input("Please enter country name to check if its a SAARC country: ")
if country.lower() in saarc:
    print(f" {country} is a member country of SAARC.")
else:
    print(f"{country} is not a member country of SAARC.")

print("Program ended")
