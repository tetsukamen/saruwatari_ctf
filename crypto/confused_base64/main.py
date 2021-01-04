import base64

crypt = "+GJX+xv1rVNIC9NIogbk9jO5zx+ICwOKcx7Z4wLZ9j+54xHvrwLZ9jkh9x+BrHmxcx7YrpZ="

wrong_table = "PXRSUegp37FAMNW8u+ysaHw94rCczo0Iqbi/GkVTBDfnYvh5KJ1lZOjx6Lt2EmdQ"

correct_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

correct_crypt = ""

for i in crypt:
    for index, w in enumerate(wrong_table):
        if i == "=":
            correct_crypt += "="
        elif i == w:
            correct_crypt += correct_table[index]

print(correct_crypt)

plain_text = base64.b64decode(correct_crypt)

print(plain_text)