
class TokenInfo(object):

    def __init__(self, idf):
        self.idf = idf
        self.lista = []

    def add_token_occurence(self, TokenOccurence):
        self.lista.append(TokenOccurence)


    def get_list_token_ocurrrence(self):
        return self.lista




