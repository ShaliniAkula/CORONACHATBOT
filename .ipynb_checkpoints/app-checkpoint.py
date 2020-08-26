from chatbotF import *
#from chatbotTK import *
#from covidbot import *
#import chatbotTK as c
import io
import string


from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    #return str(c.chat(userText))



    #return str(c.chatResponse(userText))
    return str(chatbot.get_response(userText))



if __name__ == "__main__":
    app.run() 