from chatbotTK import chat
import sqlite3
import random
#import string

from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'


#initially should land on this HOME page
@app.route("/")
def homePage():


        userCount = random.randint(0,100)
        print("count --", userCount)
        return render_template("home.html", userCount = userCount)


#on "lets chat" button click goto chatbot/index page
@app.route('/CovidChatbot')
def chatbotIndex():
    return render_template('index.html')


@app.route("/get")
def get_bot_response():
    print("in getbotresponse")
    userText = request.args.get('msg')
    print("usertext:",userText)
    return str(chat(userText))
    #return str(c.chatResponse(userText))
    #return str(chatbot.get_response(userText))


#on "back" buuton go to home page
@app.route("/home")
def landHome():
    print("----------In Home-----------")
    return render_template("home.html")


#on Click of Feedback button redirect to Feedback.html
@app.route("/feedback")
def feedback():
    return render_template("feedback.html")


@app.route("/feedbackSubmit", methods=['POST'])
def feedbackSubmit():
    print("-----------In Feedback Submit------------")
    if request.method == 'POST':

        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        mobile_no = request.form['mobile_no']
        understood_val= request.form['understood']
        relaible_val=request.form['relaible']
        # avg_rating=((understood_val+relaible_val)/2)
        feedback_text = request.form['feedback']

        print(fname,lname,mobile_no,email,feedback_text)

        sum_val = int(understood_val) + int(relaible_val)
        average = sum_val/2

        connection = sqlite3.connect('db/CovidDB.db', timeout=5)
        print("------------Database Connection Successfull------------")

        cursor = connection.cursor()
        print("-----------Database cursor-----------")

        cursor.execute('''CREATE TABLE IF NOT EXISTS CovidBotFinal(FIRSTNAME text, LASTNAME text, EMAIL_ID text, MOBILE_NO real, UNDERSTANDING_BOT real, RELIABILITY_BOT real,
         AVG_RATING real, FEEDBACK_COMMENTS text)''')

        cursor.execute('''INSERT INTO CovidBotFinal(FIRSTNAME, LASTNAME, EMAIL_ID, MOBILE_NO, UNDERSTANDING_BOT, RELIABILITY_BOT,
         AVG_RATING, FEEDBACK_COMMENTS) VALUES (?,?,?,?,?,?,?,?)''',
                       (fname, lname, email, mobile_no, understood_val, relaible_val, average, feedback_text))

        print('--------Inserted SUCCESSFULLY !!!-----------')
        connection.commit()
        print('------------Database Commit Successfull !!!--------------')

        sql = '''select * from CovidBotFinal'''
        cursor.execute(sql)
        print('------------Select Query Executed!!!-----------')
        rows = cursor.fetchall()
        print(rows)

        connection.close()
        print("----------Database CONNECTION CLOSED SUCCESSFULLY !!!---------")
        return render_template('home.html')
    else:
        print("in else")
        pass

if __name__ == "__main__":
    app.run(port=5000)
