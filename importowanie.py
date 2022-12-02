txt_file = open("dane.txt", "r")
file_content = txt_file.read()
content_list = file_content.split(",")
txt_file.close()