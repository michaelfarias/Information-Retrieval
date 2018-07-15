from filter_file import FilterFile

cont = 1
for i in range(74,80):
    file = open('cf' + str(i), 'r')
    text = file.read()
    file.close()
    text = text.split("\n\n")
    print(len(text))
    for t in text:
        file = open("files/"+ str(cont), "w")
        filter = FilterFile(t)
        file.write(filter.get_text_filtred())
        file.close()
        cont += 1
print("Quantidade = " + str( cont - 1))






