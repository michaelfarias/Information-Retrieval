cont = 1
file = open('cfquery', 'r')
text = file.read()
file.close()
text = text.split("\n\n")
for t in text:
    file = open("queries/" + str(cont), 'w')
    file.write(t)
    file.close()
    cont += 1
print("Quantidade = " + str(cont - 1))