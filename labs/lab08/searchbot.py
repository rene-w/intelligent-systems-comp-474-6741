import gzip
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_file(path): 
    g = gzip.open(path, 'r') 
    for l in g: 
        yield eval(l)

res = read_file('qa_Appliances.json.gz')

question_list = []
answer_list = []
for i in res:
    question_list.append(i['question'])
    answer_list.append(i['answer'])

question_dataset = np.asarray(question_list)

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(question_dataset)

input_question = input("What is your question: ")

if "?" in input_question:
    input_question = input_question.split("?",1)[0].strip()

search_tfidf_vector = tfidf_vectorizer.transform([input_question])

similar_questions = cosine_similarity(search_tfidf_vector,tfidf_matrix)
print("Cosine search scores:", similar_questions)

# Print the question which has the highest similarity score
index = np.where(similar_questions.T == np.max(similar_questions.T))

print("Similar question to user's question: ", question_list[int(index[0])])
print("Answer given to the similar question: ", answer_list[int(index[0])])

# Printing the top 5 questions similar to the user input
ranking_document_index = sorted(range(len(similar_questions.T)),key=similar_questions.T.__getitem__, reverse=True)

print("Top-5 similar questions to the user's question")
for idx, rowId in enumerate(ranking_document_index[:5]):
    print("\t%s. %s"%(idx+1,question_dataset[rowId]))
    


