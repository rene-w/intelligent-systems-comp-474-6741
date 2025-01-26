import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Concordia is one of the three universities in Quebec where English is the primary language of instruction (the others being McGill University and Bishops University).")

token_list =[]
for token in doc:
    print(token.text, token.lemma_, token.tag_, token.dep_)
    token_list.append(token.text)

text1 = """Superman was born on the planet Krypton and was given the name Kal-El at birth. As a baby, his parents sent him to Earth in a small spaceship moments before Krypton was destroyed in a natural cataclysm. His ship landed in the American countryside, near the fictional town of Smallville. He was found and adopted by farmers Jonathan and Martha Kent, who named him Clark Kent. Clark developed various superhuman abilities, such as incredible strength and impervious skin. His adoptive parents advised him to use his abilities for the benefit of humanity, and he decided to fight crime as a vigilante. To protect his privacy, he changes into a colorful costume and uses the alias "Superman" when fighting crime. Clark Kent resides in the fictional American city of Metropolis, where he works as a journalist for the Daily Planet. Superman's supporting characters include his love interest and fellow journalist Lois Lane, Daily Planet photographer Jimmy Olsen and editor-in-chief Perry White. His classic foe is Lex Luthor, who is either a mad scientist or a ruthless businessman, depending on the story."""

####### Sentences ###################### You can try the solution in the documentation too.
doc1 = nlp(text1)
sent_spans = list(doc1.sents)
for sentence in sent_spans:
    print(sentence)

########## Dependency ###################
# displacy.serve(doc, style="dep")

######## NER ###########################
text2 = "Apple is looking at buying U.K. startup for $1 billion"
doc2 = nlp(text2)
for ent in doc2.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

text3 = "European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices"
doc3 = nlp(text3)
options = {"ents": ["ORG"]}
displacy.serve(doc3, style="ent", options=options)