import glob
from text_file_document import TextFileDocument
from token_info import TokenInfo
from token_occurence import TokenOccurence
from document_reference import DocumentReference
import math
import pickle
import sys
import os

class BuildIndex:

    def __init__(self):
        self.dict_hash_code = {}
        self.dict_document_max_freq = {}
        self.dict_document = {}

    def create_index(self):

        # print(os.listdir("stories/"))
        for file in os.listdir(sys.argv[1]):

            self.dict_document_max_freq[file] = 0
            hash_table_vector = TextFileDocument(sys.argv[1]+file).to_vector()

            d_reference = DocumentReference(file, 0.0)

            for token in hash_table_vector.keys():
                frequency = hash_table_vector.get(token)

                if token in self.dict_hash_code:
                    t_occurence = TokenOccurence(d_reference, frequency)
                    token_info = self.dict_hash_code[token]
                    token_info.add_token_occurence(t_occurence)

                else:
                    self.dict_hash_code[token] = TokenInfo(0.0)
                    t_occurence = TokenOccurence(d_reference, frequency)
                    token_info = self.dict_hash_code[token]
                    token_info.add_token_occurence(t_occurence)


        # Calculando o idf
        for token in self.dict_hash_code.keys():
            value = self.dict_hash_code.get(token)
            number_of_documents = os.listdir(sys.argv[1]).__len__()
            df = len(value.get_list_token_ocurrrence())
            value.idf = self.calculate_idf(number_of_documents, df)


        #Computando o tamanho dos documentos

        for token in self.dict_hash_code.keys():
            weight_idf = self.dict_hash_code.get(token).idf
            for value in self.dict_hash_code.get(token).get_list_token_ocurrrence():
                counter = value.count
                # obs nao eh mais e sim vezes >>>>>>>>>>>>>>>>
                value.document_reference.length += (weight_idf * counter) ** 2
                self.dict_document[value.document_reference.file] = value.document_reference
                self.max_term(value.document_reference.file, counter)
                value.document_reference.max_freq = self.dict_document_max_freq[value.document_reference.file]
                self.dict_document[value.document_reference.file] = value.document_reference

        #Configurando tamanho do documento com raiz quadrada
        for document_reference in self.dict_document.keys():
            length = self.dict_document.get(document_reference).length
            self.dict_document.get(document_reference).length = math.sqrt(length)


        pickle_out = open("index.pickle","wb")
        pickle_out_document = open("document_reference.pickle", "wb")
        pickle.dump(self.dict_document, pickle_out_document)
        pickle.dump(self.dict_hash_code,pickle_out)
        pickle_out.close()

    #Funcao para calculo do IDF
    def calculate_idf(self, total_number_of_ducuments, df):
        return math.log(total_number_of_ducuments / df,10)



    def max_term(self, file, value):
        if(self.dict_document_max_freq[file]  < value):
            self.dict_document_max_freq[file] = value


    def get_document_max_freq(self, filename):
        return self.dict_document_max_freq[filename]

    def get_length_document(self, filename):
        value = self.dict_document[filename]
        return value.length

# a = os.listdir(sys.argv[1])
# o = open(sys.argv[1]+a[0],'r')
# print(o.read())

index = BuildIndex()

print("Processando...")
print("*****************")
index.create_index()
print("Finalizado!")


