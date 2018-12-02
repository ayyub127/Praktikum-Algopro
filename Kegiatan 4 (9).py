import shelve

data = shelve.open("Ayyub")
print(data["databaru"][0])
print(data["databaru"][1])
print(data["databaru"][2])
print(data["databaru"][3])
