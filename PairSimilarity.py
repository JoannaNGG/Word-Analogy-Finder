import gensim.downloader as api
import numpy as np

print("\nLoading the Word2Vec Model, please wait...")
model = api.load("word2vec-google-news-300")
print("Model Loaded.\n")

def relation_similarity(A, B, C, D):
    vec1 = model[B] - model[A]
    vec2 = model[D] - model[C]
    similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    return similarity

#get input pairs
print("Enter your first word pair (A:B): ")
pair1 = input().strip().lower()
A, B = [w.strip() for w in pair1.split(":")]

print("Enter your second word pair (C:D): ")
pair2 = input().strip().lower()
C, D = [w.strip() for w in pair2.split(":")]

#compute relation similarity
relation_sim = relation_similarity(A, B, C, D)

print(f"\nRelationship similarity between ({A}:{B}) and ({C}:{D}) = {relation_sim:.3f}")

#threshold for approximately the same
threshold = 0.8
if relation_sim >= threshold:
    print("The pairs have approximately the same semantic relationship.")
else:
    print("The pairs do NOT have the same semantic relationship.")