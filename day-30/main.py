# File Not Found
# with open("some-file.txt") as file:
#     content = file.read()

# Key Error
# dict = {"key": "value"}
# print(dict["potato"])

# List Error
# list = [1, 2, 3]
# print(list[4])

# Type Error
# text = "abc"
# print(text + 5)
#
# try:
#     file = open("a_file.txt")
#     dict = {"key": "value"}
#     print(dict["potato"])
# except FileNotFoundError:
#     # print("THERE WAS AN ERROR")
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
#     raise KeyError("Some message")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)