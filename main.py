import spacy
import nltk
from nltk.corpus import wordnet
from nltk.wsd import lesk

nltk.download('wordnet')
prompt1 = "I want a family car"
prompt2 = "Car for college student"
prompt4= "a cool car"
prompt5 = "vehicles for travel and adventure"
prompt6 = "eco-friendly and fuel-efficient car"
prompt7 = "luxury car that is spacious"

categories = ["sporty", "adaptable", "affordable", "hybrid", "big", "fast", "efficient"]

nlp = spacy.load('en_core_web_sm')

#Remove Stop Words
prompt_tokens = []
stopwords = spacy.lang.en.stop_words.STOP_WORDS
for i in prompt1.split():
    if i not in stopwords:
        prompt_tokens.append(i)

print(prompt_tokens)

# Remove All Types of Unnecessary Words
pos_tags_to_remove = {'VERB', 'PRON', 'ADP'} 
doc = nlp(' '.join(prompt_tokens))
necessary_tokens = []
for token in doc:
    if token.pos_ not in pos_tags_to_remove:
        necessary_tokens.append(token.text)
print(necessary_tokens)

baseString = ' '.join(necessary_tokens)

# similarityResults = {}
# for category in categories:
#     doc1 = nlp(category)
#     doc2 = nlp("family")
#     similarityResults[category] = doc1.similarity(doc2)

#print(similarityResults)
similarityResults = {}
for category in categories:
    similarity_score =0
    for i in necessary_tokens:
        word1 = wordnet.synset(category+'.a.01')
        word2 = wordnet.synset(i+'.n.01')
        similarity_score += wordnet.wup_similarity(word1, word2)
        
    similarityResults[category] = similarity_score/len(necessary_tokens)

print(similarityResults)