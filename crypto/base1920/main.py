import base64

with open("base1920.txt", "r") as f:
    s = f.read()
    for i in range(30):
        s = base64.b64decode(s)
    print(s)