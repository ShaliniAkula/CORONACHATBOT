#from chatbotF import chatbot
from chatbotTK import chat
import sqlite3
import string

from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'


#initially should land on this HOME page
@app.route("/")
def homePage():
    return render_template("home.html")


#on "lets chat" button click goto chatbot/index page
@app.route('/CovidChatbot')
def chatbotIndex():
    return render_template('index.html')


@app.route("/get")
def get_bot_response():
    print("In Response >>>>>>>>>>>")
    userText = request.args.get('msg')
    print("user Test ???????/", userText)
    return str(chat(userText))

    #return str(c.chatResponse(userText))
    #return str(chatbot.get_response(userText))



#on "back" buuton go to home page
@app.route("/home")
def landHome():
    print("in home")
    return render_template("home.html")


#on Click of Feedback button redirect to Feedback.html
@app.route("/feedback")
def feedback():
    return render_template("feedback.html")


@app.route("/feedbackSubmit", methods=['POST'])
def feedbackSubmit():
    print("in submit")
    if request.method == 'POST':

        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        mobile_no = request.form['mobile_no']
        feedback_text = request.form['feedback']

        print(fname,lname,mobile_no,email,feedback_text)
        connection = sqlite3.connect('db/ChatbotAwarenessNew.db', timeout=5)
        print("hello con done")

        cursor = connection.cursor()
        print("hello cursor done")
        # sql = '''CREATE TABLE IF NOT EXISTS UserLogin1(PID INTEGER PRIMARY KEY AUTOINCREMENT, FIRSTNAME VARCHAR(50),
        #                LASTNAME VARCHAR(50),EMAIL_ID VARCHAR(25) , MOBILE_NO INTEGER(15), FEEDBACK VARCHAR(300))'''

        # sql = '''INSERT INTO UserLogin1(PID, FIRSTNAME, LASTNAME, EMAIL_ID, MOBILE_NO, FEEDBACK) VALUES
        # (1, 'Trupti', 'Mane', 'manetrupti53@gmail.com', 8082342598, 'A Very good app')'''
        # cursor.execute(sql)

        cursor.execute('''INSERT INTO UserLogin1(FIRSTNAME,LASTNAME,EMAIL_ID,MOBILE_NO,FEEDBACK) VALUES (?,?,?,?,?)''',
                       (fname,lname,email,mobile_no,feedback_text))
        print('insert done')
        connection.commit()
        print('commit done')
        # sql = '''select * from UserLogin1'''
        # print('select sql')
        # cursor.execute(sql)
        # print('selct exec')
        # rows = cursor.fetchall()
        # print(rows)

        connection.close()
        print("done conn closed---------------")
        return render_template('home.html')
    else:
        print("in else")
        pass


if __name__ == "__main__":
    app.run()
