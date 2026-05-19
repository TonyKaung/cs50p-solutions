u_input = input("Enter the file name: ").lower().strip()
if(u_input.endswith(".gif")):
    print("image/gif")
elif(u_input.endswith(".jpg")):
    print("image/jpeg")
elif(u_input.endswith(".jpeg")):
    print("image/jpeg")
elif(u_input.endswith(".png")):
    print("image/png")
elif(u_input.endswith(".pdf")):
    print("application/pdf")
elif(u_input.endswith(".txt")):
    print("text/plain")
elif(u_input.endswith(".zip")):
    print("application/zip")
else:
    print("application/octet-stream")