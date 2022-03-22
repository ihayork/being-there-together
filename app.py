from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    
    m = open("message.txt","r")
    messages = m.readlines()
    numMessage = len(messages)
    
    select = random.randint(0, numMessage-1)
    return render_template("index.html", message=messages[select])

    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()

    # Render HTML with count variable
    return render_template("index.html", count=count)

@app.route('/', methods=['POST'])
def writeMessage():
    message = request.form["TEXT"]
    m = open("message.txt","a")
    m.write("\n" + message)
    return
    

if __name__ == "__main__":
    app.run()
