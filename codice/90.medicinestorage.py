SEP = ","
OPADD = "add"
OPDEL = "remove"

storage = {}

entry = input()
while entry != "":
    # get the entry
    info = entry.strip().split(SEP)
    # retrieve the quantity in the storage if there is already the medicine in the storage
    if info[0] in storage:
        qty = storage[info[0]]
    else:
        qty = 0
    if info[1] == OPADD:
        storage[info[0]] = qty + int(info[2].strip())
    else:
        storage[info[0]] = qty - int(info[2].strip())
    entry = input()

# acquisition is completed
for key, value in storage.items():
    if value > 0:
        print(key, value)
