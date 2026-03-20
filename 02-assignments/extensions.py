#Prompt user for the name and extension of a file
f_type = " ".join(input("File Name: ").lower().split())

#Check file type and display media type based on the extension of the file
if f_type.endswith(".gif"):
    print(f"image/gif")

elif f_type.endswith(".jpg"):
    print(f"image/jpg")

elif f_type.endswith(".jpeg"):
    print(f"image/jpeg")

elif f_type.endswith(".png"):
    print(f"image/png")

elif f_type.endswith(".pdf"):
    print(f"aplication/pdf")

elif f_type.endswith(".txt"):
    print(f"text/plain")

elif f_type.endswith(".zip"):
    print(f"application/zip")

else:
    print("application/octet-stream")