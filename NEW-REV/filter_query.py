class FilterQuery(object):

    def __init__(self):
        pass

    def get_query(self, text):
        query_text = text.split("\n")
        query = ""
        for i in range(1, len(query_text)):
            if query_text[i][:2] == "NR":
                break
            else:
                query = query + query_text[i]
        return query[3:]

    def get_array_docs(self, text):
        aux = 0
        docs = ""
        text = text.split("\n")
        for i in range(3, len(text)):
            if text[i][:2] == "RD":
                docs = text[i][4:]
                aux = 1
                continue
            if aux == 1:
                if text[i][4] == " ":
                    docs = docs + " " + text[i][4:]
                else:
                    docs = docs + " " + text[i][3:]
        result_docs = []
        docs = docs.replace("  ", " ")
        docs = docs.replace("  ", " ")
        docs = docs.split(" ")
        if docs[0] == "":
            docs = docs[1:]
        for i in range(0, len(docs)):
            if i % 2 == 0 and docs[i] != "":
                result_docs.append(int(docs[i]))
        return result_docs


# arq = open("cfc/queries/1", "r");
# a = arq.read()
# print(a)
# print("*******************")
# filter = FilterQuery()
# print(filter.get_query(a))
# print(filter.get_array_docs(a))
