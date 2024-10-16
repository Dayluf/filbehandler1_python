with open("read.txt", "r") as file_object:
        content = file_object.read()
        print(content)

with open("write.txt", "a") as f:
        command = input("\n")
        content = f.write(command)