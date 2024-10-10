with open("read.txt", "r") as file_object:
        content = file_object.read()
        print(content)

with open("write.txt", "a") as user_input:
        content = user_input.write(" fårhåpentligvis vil ikke teksten som allerede står der bli slettet \n")