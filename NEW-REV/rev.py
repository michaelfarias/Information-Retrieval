from text_file_document import TextFileDocument
import math
import pickle
import sys
import os
from filter_query import FilterQuery
import matplotlib.pyplot as plt




class Rev:

    def __init__(self):
        self.dict_document = {}
        self.dict_document_sorted ={}

    def recovering_index(self, query):
        arq = open('query/query.txt','w')
        arq.write(query)
        arq.close()


        hash_table_vector = TextFileDocument("query/query.txt").to_vector()

        pickle_in = open(sys.argv[1], "rb")
        index_b = pickle.load(pickle_in)

        pickle_in_doc = open("document_reference.pickle", "rb")
        dict_doc = pickle.load(pickle_in_doc)

        weight_list = []
        for token in hash_table_vector.keys():
            max_freq = max(hash_table_vector.keys(),key = hash_table_vector.get)

            tf = hash_table_vector.get(token) / hash_table_vector.get(max_freq)
            weight = hash_table_vector.get(token) * tf
            weight_list.append(weight_list)

            if index_b.__contains__(token):
                #idf
                idf = index_b[token].idf
                for value in index_b[token].get_list_token_ocurrrence():
                #tf de O
                    doc = dict_doc[value.document_reference.file]
                    c = value.count / doc.max_freq

                    if value.document_reference.file  not in   self.dict_document:
                        self.dict_document[value.document_reference.file] = 0.0

                self.dict_document[value.document_reference.file] += (weight*idf*c)



        for document in self.dict_document.keys():

            score = self.dict_document.get(document)
            value = dict_doc[document]
            length = value.length
            try:
                self.dict_document[document] = self.dict_document.get(document) / (score*length)

            except ZeroDivisionError:
                pass
                # self.dict_document[document] = 0.0
                # print("Teve divisao por zero!")


        self.dict_document_sorted = sorted(self.dict_document.keys(), key = self.dict_document.get)

        return self.dict_document_sorted


    def compute_weight(self, weight_list):
        sum = 0
        for value in weight_list:
            sum += value**2

        return math.sqrt(sum)

    def to_clear(self):
        self.dict_document = {}
        self.dict_document_sorted = {}





rev = Rev()

is_true = True

n = 5
while is_true:
    query = raw_input("Insira sua consulta: ")
    print("Pesquisando...")

    if len(query) == 0:
        is_true = False

    for name_doc in rev.recovering_index(query).__getslice__(0,n):
        print(name_doc)

    to_next = True

    while to_next:

        comand = raw_input("1)Mostrar as proximas "+ str(n)+ " recuperacoes: ")

        if len(comand) == 0:
            to_next = False

        if(comand == "1"):
            for name_doc in rev.recovering_index(query).__getslice__(n, n + 5):
                print(name_doc)

    n += 5

# def calculate_recall(num_doc_rele_retr, num_total_rele_retri):
#
#     try:
#         recall = num_doc_rele_retr / num_total_rele_retri
#     except ZeroDivisionError:
#         recall = 0.0
#
#     return recall
#
# def calculate_precision(num_doc_rele_retr, num_total_retri):
#     recall = 0.0
#     try:
#         recall = num_doc_rele_retr / num_total_retri
#     except ZeroDivisionError:
#         recall = 0.0
#
#     return recall
#
# def precision_r(position_num_rel, num_docs_rel):
#
#     try:
#         div = position_num_rel / num_docs_rel
#     except ZeroDivisionError:
#         div = 0.0
#
#     return div
#
#
#
#
# queries = os.listdir("cfc/queries/")
#
# quant = int(input("Quantas consultas deseja realizar ? "))
#
# filter = FilterQuery()
#
# dict_document = {}
# dict_precision_r = {}
# for i in range(0, quant):
#
#     arq = open('cfc/queries/' + queries[i], 'r')
#     query = arq.read()
#     list_document = rev.recovering_index(filter.get_query(query))
#     rev.to_clear()
#     list_document = map(int, list_document)
#     tuple_doc_cob_prec = []
#     cont_doc_rel = 0.0
#     cont_retrie = 0.0
#     sum_precision = 0.0
#     sum_recall = 0.0
#     cont = 0
#     for document in list_document[0:50]:
#         cont_retrie += 1.0
#         if document in filter.get_array_docs(query):
#             cont_doc_rel += 1.0
#             tuple_doc_cob_prec.append((document, calculate_recall(cont_doc_rel, len(filter.get_array_docs(query))), calculate_precision(cont_doc_rel, cont_retrie)))
#         else:
#             tuple_doc_cob_prec.append((document, 0.0, 0.0))
#
#         aux = tuple_doc_cob_prec[cont]
#         sum_recall += aux[1]
#         sum_precision += aux[2]
#         cont += 1
#
#     dict_precision_r[i] = precision_r(cont_doc_rel, len(filter.get_array_docs(query)))
#     try:
#         dict_document[queries[i]] = (sum_recall / float(cont), sum_precision / float(cont))
#     except ZeroDivisionError:
#         pass
#         # dict_document[queries[i]] = (0.0, 0.0)
# #
# #
# #
# # arq = open("dataGraph/data2", "wb")
# # pickle.dump(dict_document, arq)
# # arq.close()
# #
#
# x = []
# y = []
#
# #   PRECISAO MEDIA
# for key in dict_document.keys():
#     x.append(dict_document.get(key)[0])
#     y.append(dict_document.get(key)[1])
#
#
# plt.plot(x, y)
# plt.legend()
# plt.title("Precisao Media")
# plt.xlabel("Cobertura")
# plt.ylabel("Presicao")
# plt.savefig('precisaoMedia[100].2.png')
# plt.show()
#
#
# #
# # arq1 = open("dataGraph/data1","rb")
# # dict1 = pickle.load(arq1)
# # arq1.close()
# #
# #
# # #   PRECISAO MEDIA (NoStem - Stem)
# # for key in dict1.keys():
# #     x.append(dict1.get(key)[0])
# #     y.append(dict1.get(key)[1])
# #
# # plt.plot(x, y, color='blue', label = 'com stemmer')
# #
# # arq2 = open("dataGraph/data2","rb")
# # dict2 = pickle.load(arq2)
# # arq2.close()
# #
# # x1 = []
# # y1 = []
# #
# # for key in dict2.keys():
# #     x1.append(dict2.get(key)[0])
# #     y1.append(dict2.get(key)[1])
# #
# # plt.plot(x1, y1, color='red',  label = 'sem stemmer')
# #
# # plt.legend()
# # plt.title("Precisao Media")
# # plt.xlabel("Cobertura")
# # plt.ylabel("Presicao")
# # plt.savefig('precisaoMediaCSStemmer.png')
# # plt.show()
#
#
#
#
# #   PRECISAO R
# # for key in dict_precision_r.keys():
# #     x.append(key)
# #     y.append(dict_precision_r.get(key))
# #
# #
# # plt.plot(x, y,'r')
# # plt.title("Precisao R")
# # plt.savefig('precisaoR.png')
# # plt.show()