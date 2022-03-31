from flask import Flask
app=Flask(__name__)

@app.route("/emicon")
def rakesh1():
    return "Emicon and Emicon Clients, Welcome!"
    

@app.route("/<path:text>")
def rakesh2(text):
    return "Request URL is:  %s " %text


@app.route("/")
def rakesh3():
    return "Hello! how are you"


if __name__=='__main__':
    app.run(debug=True) 