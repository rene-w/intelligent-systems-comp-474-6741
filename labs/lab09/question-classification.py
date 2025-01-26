import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from collections import Counter
import spacy
import matplotlib.pyplot as plt

nlp = spacy.load("en_core_web_sm")


def create_features(text):
    doc = nlp(text)
    pos_list = [token.tag_ for token in doc]  # Create a list with all the POS tags in the text
    pos_count_dict = Counter(pos_list)  # Count the number of POS tags withing the POS list
    entity_list = [token.label_ for token in doc.ents]  # Create a list with all the entities withing the text
    ent_count_dict = Counter(entity_list)  # Count the number of entity types withing the entity list
    root_lemma = [token.lemma_ for token in doc if token.dep_ == "ROOT"][0]  # Lemma of the root token in the text
    sentence_length = sum(len(token) for token in doc)  # Length of the text (number of characters within the text)

    return [root_lemma, pos_count_dict['WP'], pos_count_dict["WRB"],
            ent_count_dict["PERSON"], ent_count_dict["GRE"],
            ent_count_dict['ORG'], sentence_length]


corpus = [
    'Who is Bill Gates',
    'Where is Concordia located',
    'What is AI',
    'What city is McGill located in',
    'Who is McGill'
]

features = []
for text in corpus:
    features.append(create_features(text))

feature_mtrx = np.array(features)  # Convert the feature matrix to a numpy array.

le = LabelEncoder()
feature_mtrx[:, 0] = le.fit_transform(feature_mtrx[:, 0])

# 0=Who, 1= Where, 2=What
y = np.array([0, 1, 2, 2, 0])

clf = DecisionTreeClassifier(random_state=0)
clf.fit(feature_mtrx, y)

q = "Who is Obama"

q_vect = np.array([create_features(q)])
q_vect[:, 0] = le.transform(q_vect[:, 0])

print(clf.predict(q_vect))

plt.figure()
plot_tree(clf, filled=True, feature_names=["root", "wp_count", "wrb_count", "person", "gre", "org", "length"])
plt.show()
