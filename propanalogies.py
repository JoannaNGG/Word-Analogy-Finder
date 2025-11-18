import gensim.downloader as api

model = api.load("word2vec-google-news-300")

pos1 = input("Enter the first positive word: ")
pos2  = input("Enter the second positive word: ")
neg1 = input("Enter the negative word: ")

result = model.most_similar(
    positive = [pos1, pos2],
    negative = [neg1],
    topn = 5
)

# Round scores to 3 decimals
rounded_result = [(word, round(score, 3)) for word, score in result]
print(rounded_result)