# Word Analogy Finder
This simple Python program uses a pretrained Word2Vec Google News model to compute word analogies. 

It allows the user to enter two postive words and one negative word, then returns the top 5 most similar words based on vector arithmetic. 

An example analogy:
man :king :: woman : queen 

**Steps**
**Ensure that you are in the correct directory**
**Optional, but recommended:** Create a venv (python -m venv nameofvenv)
If using a vevn, ensure the correct interpreter is selected otherwise a module not found error may occur.

**Install requirements.txt:** pip install -r requirements.txt

**Run the Program**

**Example Analogy**:
man : king :: woman : ?

First positive word: king
Second Positive word: woman
First Negative word: man
Expected result: queen (as the top result)