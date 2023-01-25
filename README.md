
# **spaCy sentence similarity**
    Test the spaCy sentence similarity using the 'en_core_web_lg' model.
    

# **Description:**
    *This program is a demo of spaCy capabilities to find similarity between sentences.*
    It has a prebuilt already seen movie description which it is comparing with other movies description
    supplied from the movies.txt User is asked to choose one from the 4 methods used to achive this
    and notice the difference in results.
    *Methodes:*
            - **Normal** - Perform a direct similarity check 
            
            - **Stop words** - Perform the similarity check after we remove all stop words 
            (assume stop words have less relevance)
            
            - **Restrictive** - Perform the similarity check using only 'NOUN', 'PROPN' 
            (assume the most relevant words are 'NOUN', 'PROPN')
            
            - **All** - Use all 3 above and the result will be an average of all individual scores
    

# **Require:**
    Require spaCy module and model 'en_core_web_lg' 
    Installation details page is:
    https://spacy.io/usage
    

# **Installation:**
    pip install -U spacy
    python3 -m spacy download en_core_web_lg
    
# **Running:**
    whatch_next.py

# **Credits:**
    Alin Rizea
    https://www.linkedin.com/in/alin-rizea-b10368104/
