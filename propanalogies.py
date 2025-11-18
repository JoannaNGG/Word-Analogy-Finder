import gensim.downloader as api

print("\nLoading the Word2Vec Model, please wait...")
model = api.load("word2vec-google-news-300")
print("Model Loaded.\n")


analogy = input("Enter your analogy in format A:B::C:? ")

left, right = analogy.split("::")
A, B = left.split(":")
C, _ = right.split(":")

#Compute B - A + c
result = model.most_similar(
    positive = [B.strip(), C.strip()],
    negative = [A.strip()],
    topn = 5
)

#Round scores to 3 decimals
roundResult = [(word, round(score, 3)) for word, score in result]
print(roundResult)