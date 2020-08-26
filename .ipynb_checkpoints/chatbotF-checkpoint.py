
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('CoronaBot',storage_adapter='chatterbot.storage.SQLStorageAdapter',
                   logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
                  )


for files in os.listdir('/Users/shravankumarakula/Desktop/CORONACHATBOT/training_data/'):
    training_data = open('/Users/shravankumarakula/Desktop/CORONACHATBOT/training_data/'+files,'r',errors = 'ignore').readlines()
    trainer = ListTrainer(chatbot)
    trainer.train(training_data)
    #print("Training completed")


# Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
)



