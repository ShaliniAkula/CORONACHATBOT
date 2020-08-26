
import io
import random
import string # to process standard python strings
#import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages

# uncomment the following only the first time
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only


#Reading in the corpus
f=open('/Users/shravankumarakula/Desktop/CORONACHATBOT/training_data/CovidTxtPara.txt','r',errors = 'ignore')
#raw = f.read().lower()
raw=f.read()
#TOkenisation
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences
word_tokens = nltk.word_tokenize(raw)# converts to list of words

# Preprocessing
lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
Basic_Q = ("What is Coronavirus ?","what is coronavirus ?","What is coronavirus ?","What is COVID-19", "what is covid-19 ?","What is covid-19 ?")
Basic_Ans = ("COVID-19 is a highly infectious respiratory disease caused by a new coronavirus. The disease was discovered in China in December 2019 and has since spread around the world, causing an unprecedented public health crisis.For health, safety, and medical emergencies or updates on the novel coronavirus pandemic, please visit the CDC (Centers for Disease Control and Prevention) and WHO (World Health Organization).")


def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def basic(sentence):
    for word in Basic_Q:
        if sentence.lower() == word:
            return Basic_Ans


# Generating response
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


def chat(user_response):
    user_response = user_response.lower()
    keyword = " module "
    keywordone = " module"
    keywordsecond = "module "

    if (user_response != 'bye'):
        if (user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            # print("ROBO: You are welcome..")
            return "You are welcome.."

        else:
            if (greeting(user_response) != None):
                # print("ROBO: ",end="")
                # print(responseone(user_response))
                return greeting(user_response)
            elif (basic(user_response) != None):
                return basic(user_response)
            else:
                # print("ROBO: "+greeting(user_response))
                return response(user_response)
                sent_tokensone.remove(user_response)







    else:
        flag = False
        # print("ROBO: Bye! take care..")
        return "Bye! take care.."