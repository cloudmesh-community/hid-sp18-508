#from nltk import word_tokenize, pos_tag
import spacy
nlp = spacy.load('en_core_web_sm')

class LING(object):
    def __init__(self, input):
        #self._input = input
        #self._tokens = word_tokenize(self._input)
        self._spacyDoc = nlp(input)

    def tokens(self):
        return " , ".join([str(w.text) for w in self._spacyDoc])
        #return self._tokens

    def pos(self):
        return " , ".join([str((w.text,w.pos_)) for w in self._spacyDoc])
        #return pos_tag(self._tokens)

    def depparse(self):
        return " , ".join([str((w.text,w.dep_, w.head.text)) for w in self._spacyDoc])

    def entity(self):
        return " , ".join([str((w.text, w.ent_type_)) for w in self._spacyDoc])


if __name__ == '__main__':
    ling = LING("Tim Cook bought Apple")

    print(ling.tokens())
    print(ling.pos())
    print(ling.depparse())
    print(ling.entity())