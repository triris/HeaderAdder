header_file = "header.txt"
content_file = "content.txt"

with open (content_file, "r+") as content_file:
    contents = content_file.readlines()
    content_file.seek(0)
    with open(header_file, "r+") as header_file:
        for line in header_file:
            content_file.write(line)
    content_file.write("\n")
    content_file.writelines(contents)



    

    




