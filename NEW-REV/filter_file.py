class FilterFile(object):

    def __init__(self, text):
        self.text = text

    def get_text_filtred(self):
        textResult = ""
        text = self.text.split("\n")
        for i in range(3, len(text)):
            if text[i][:2] == "AU" or text[i][:2] == "TI" or text[i][:2] == "MJ" or text[i][:2] == "MN" or text[i][:2] == "AB":
                textResult = textResult + text[i][3:]
            else:
                if text[i][:2] == "RF":
                    break
                if text[i][:2] != "SO":
                    textResult = textResult + text[i][3:]
        return textResult


# arq = open("cfc/files/1","r")
# t = arq.read()
# print(t)
# print("*****************")
#
# filter = FilterFile(t)
# print filter.get_text_filtred()