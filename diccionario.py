d = {
    "1":"uno",
    "2":"dos",
    "3":"tres",
    "4":"cuatro"
}
number = input("Give me a number: ")
msg = ""
for i in number:
    msg += d[i]+" "
print(msg)