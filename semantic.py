import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare ="Why is my cat on the car"
sentences = ["where did my dog go","Hello, there is my car","I\'ve lost my car in my car","I\'d like my boat back","I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence +" - ",similarity)


"One interesting aspect of the similarities between cat, monkey, and banana is that they all have a connection to each other in terms of their biological or ecological significance."

"This is an example of how spaCy's model can be used to identify similarities or dissimilarities between two sets of long texts. The code imports the spacy module and loads the 'en_core_web_md' model. The model is then used to analyze two sets of long texts: complaints and recipes. The similarity of each complaint and recipe instruction to every other complaint and recipe instruction is calculated using spaCy's similarity method, and the results are printed to the console."