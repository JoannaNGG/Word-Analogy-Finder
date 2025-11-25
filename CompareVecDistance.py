import gensim.downloader as api

print("\nLoading the Word2Vec Model, please wait...")
model = api.load("word2vec-google-news-300")
print("Model Loaded.\n")

analogy = input("Enter your analogy in format 'A:B::C:?'\n")

left, right = analogy.split("::")
A, B = left.split(":")
C, _ = right.split(":")

#Compute B - A + C
result = model.most_similar(
    positive=[B.strip(), C.strip()],
    negative=[A.strip()],
    topn=5
)

roundResult = [(word, round(score, 3)) for word, score in result]
print(roundResult)

#Compare top 1 result with "male/female"
top_word = result[0][0]

sim_male = model.similarity(top_word, "male")
sim_female = model.similarity(top_word, "female")

print(f"\nSimilarity of '{top_word}' to 'male': {sim_male:.3f}")
print(f"Similarity of '{top_word}' to 'female': {sim_female:.3f}")