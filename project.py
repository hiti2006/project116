from flask import Flask
app=Flask(__name__)
@app.route("/")
def first_class():
    return "I'm Hiti,I am an 18year old"

@app.route("/hitisdad")
def second():
    return "Hiti lives with her dad"

app.run()