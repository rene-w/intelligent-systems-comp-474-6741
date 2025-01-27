import spacy
from  spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)
pattern = [{'TAG': 'NNP', 'OP': '*'},
           {'TAG': 'NNPS', 'OP': "*"},
           {'ORTH': 'University'}]

matcher.add("uni_identifier", [pattern])

text = """Concordia University (French: Université Concordia; commonly referred to as Concordia) is a public comprehensive research university located in Montreal, Quebec, Canada. Founded in 1974 following the merger of Loyola College and Sir 
George Williams University, Concordia is one of the three universities in Quebec where English is the primary language of instruction (the others being McGill University and Bishops University). As of the 2018–19 academic year, there were 46,829 students enrolled in 
credit courses at Concordia, making the university among the largest in Canada by enrollment. The university has two campuses, set approximately 7 kilometres (4 miles) apart: Sir George Williams Campus is the main campus, located in Downtown 
Montreal in an area known as Quartier Concordia; and Loyola Campus in the residential district of Notre-Dame-de-Grâce. """

doc = nlp(text)

matches = matcher(doc)

for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print(match_id, string_id, start, end, span.text)