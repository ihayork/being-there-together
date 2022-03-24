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

    # Render HTML with count variable
    return render_template("index.html", message=messages[select], count=count)

@app.route("/form", methods=['GET', 'POST'])
def form():
    
    if(request.method == 'POST'):
        message = request.form['TEXT']
        m = open("message.txt","a")
        m.write("\n" + message)
        m.close()
    
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

    # Render HTML with count variable
    return render_template("index.html", message=messages[select], count=count)

if __name__ == "__main__":
    app.run()
