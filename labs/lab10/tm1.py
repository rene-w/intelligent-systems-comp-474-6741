import spacy
from spacy.language import Language

nlp = spacy.load("en_core_web_sm")
@Language.component("custom_title_counter")
def custom_title_counter(doc):
    title_count = sum([1 for token in doc if token.is_title])
    print(f"This document has {title_count} title cased tokens!!!")
    return doc

print(nlp.pipe_names)
nlp.add_pipe("custom_title_counter", last=True)

print(nlp.pipe_names)

text = """Concordia University (French: Université Concordia; commonly referred to as Concordia) is a public comprehensive research university located in Montreal, Quebec, Canada. Founded in 1974 following the merger of Loyola College and Sir 
George Williams University, Concordia is one of the three universities in Quebec where English is the primary language of instruction (the others being McGill and Bishop's). As of the 2018–19 academic year, there were 46,829 students enrolled in 
credit courses at Concordia, making the university among the largest in Canada by enrollment. The university has two campuses, set approximately 7 kilometres (4 miles) apart: Sir George Williams Campus is the main campus, located in Downtown 
Montreal in an area known as Quartier Concordia; and Loyola Campus in the residential district of Notre-Dame-de-Grâce. """

doc = nlp(text)
