import nltk

sent="Mark is studying at Stanford University in California"

tokens=nltk.word_tokenize(sent)
tagged=nltk.pos_tag(tokens)
entities=nltk.chunk.ne_chunk(tagged)

print(entities)

