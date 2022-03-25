from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():

    m = open("message.txt","r")
    messages = m.readlines()
    numMessage = len(messages)
    m.close()
    
    select = random.randint(0, numMessage-1)
    
    f = open("count.txt", "r")
    count = int(f.read()) + 1
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()
    
    errorMessage = "Please enter a message with more than 0 characters and no more than 120 characters."

    # Render HTML with count variable
    return render_template("index.html", message=messages[select], count=count)

@app.route("/form", methods=['GET', 'POST'])
def form():
    
    if(request.method == 'POST'):
        message = request.form['message']
        if(len(message) > 120 or len(message) < 1):
            errorMessage = "Please make sure you enter a message with more than 0 characters, and no longer than 120 characters.\nYour last message had: " + len(message) + " characters. Please adjust the content of your message."
        else:
            m = open("message.txt","a")
            m.write("\n" + message)
            m.close()
            errorMessage = "Your message has been received!"
    
    m = open("message.txt","r")
    messages = m.readlines()
    numMessage = len(messages)
    m.close()
    
    select = random.randint(0, numMessage-1)
    
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Render HTML with count variable
    return render_template("form.html", message=messages[select], count=count, errorMessage=errorMessage)

@app.route("/messages")
def messages():
    
    m = open("message.txt","r")
    output = m.readlines()
    
    return render_template("messages.html", output=output)

if __name__ == "__main__":
    app.run()
