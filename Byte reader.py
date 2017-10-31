with open("msg1.dat", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    print(data)

with open("msg2.dat", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    print(data)