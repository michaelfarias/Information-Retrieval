from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem.porter import PorterStemmer as stemmer
import re

class TextFileDocument():

    def __init__(self, filename):
        self.filename = filename


    def tokenize(self):
        arq = open(self.filename, 'r')
        words = arq.read()
        arq.close()
        words = re.sub('[^A-Za-z]+', ' ', words)
        word_tokens = word_tokenize(words.lower())
        stop_words = set(stopwords.words('english'))

        filtered_sentence = [w for w in word_tokens if not w in stop_words]

        return filtered_sentence

    def to_vector(self):
        frequency_toke = list()
        for toke in self.tokenize():
          frequency_toke.append(stemmer().stem(toke))
          # frequency_toke.append(toke)

        return FreqDist(frequency_toke)

# a = TextFileDocument("./stories/00a39c134080b6f215a81c15d46c3ac7cc7bdcf3.story")
# for k in a.calculate_frequency():
#     print(str(k) + ' - ' + str(a.calculate_frequency().get(k)))





