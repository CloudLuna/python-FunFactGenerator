d = {
    "1":"uno",
    "2":"dos",
    "3":"tres",
    "4":"cuatro"
}
number = input("Give me a number: ")
msg = ""
msg2 = ""
for ch in number:
    msg += d.get(ch,"-") +" "
    msg2 += d.get(ch,ch) + " "
print(msg)
print(msg2)