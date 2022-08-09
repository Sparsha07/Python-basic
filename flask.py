from flask import Flask 
app = Flask(__name__) 
@app.route("/") 
def hello_world(): 
 return "<p><B>Hello SPARSHA Here <br> SE COMPC 19</B> </p>" 
if __name__ == "__main__": 
 app.run(debug=True)
