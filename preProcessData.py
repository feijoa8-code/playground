import re
import unidecode
import string
import contractions
import spacy
from nltk.tokenize import word_tokenize
sp = spacy.load('en_core_web_sm')


def filterStopWords(data: string):
    all_stopwords = sp.Defaults.stop_words
    # all_stopwords.remove("not")
    text_tokens = word_tokenize(data)
    tokens_without_sw = [
        word for word in text_tokens if not word in all_stopwords]
    return " ".join([token for token in tokens_without_sw])


def lemmatization(data: string):
    doc = sp(data)
    return " ".join([token.lemma_ for token in doc])


def filterSpecialChar(data: list):
    alphaNumericData = []
    for x in data:
        alphaNumericData.append(x.translate(
            str.maketrans('', '', string.punctuation)))
    return alphaNumericData


def preprocessData(data: list):
    data = [''.join(x) for x in data]  # convert to list of string
    data = list(dict.fromkeys(data))  # remove duplicate values
    data = list(filter(None, data))   # remove empty values
    data = filterSpecialChar(data)  # remove special characters
    data = [re.sub("(<.*?>)", "", word) for word in data]  # remove html markup
    # Convert accented characters to ASCII characters
    data = [unidecode.unidecode(word) for word in data]
    data = [word.strip() for word in data]  # remove trailing space
    data = [contractions.decontracted(word)
            for word in data]  # handled contractions
    data = [filterStopWords(word) for word in data]  # filter StopWords
    data = [lemmatization(word) for word in data]  # Lemmatization
    data = appendIfAbsent('.', data)        # add . in end of line
    data = [word.lower() for word in data]  # lower case
    data = [word.replace('-pron-', '') for word in data]
    data = [word.strip() for word in data]  # remove trailing space

    return data


def appendIfAbsent(s, data):
    fixedData = []
    for x in data:
        fixedData.append(
            x.lower() + s) if not x.endswith(s) else fixedData.append(x.lower())
    return fixedData
