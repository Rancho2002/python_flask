from flask import Flask, jsonify

app = Flask(__name__)

def binary(n:int)->str:
    ans=""
    while n:
        ans=str(n%2)+ans
        n=n//2

    return ans

def octal(n:int)->str:
    ans=""
    while n:
        ans=str(n%8)+ans
        n=n//8

    return ans

def hexa(n:int)->str:
    ans=""
    while n:
        digit=n%16
        if digit>9:
            digit=chr(65+digit-10)

        ans=str(digit)+ans
        n=n//16

    return ans

@app.route("/")
def index():
    return "Hello World"

@app.route("/convert/<int:n>",methods=['GET','POST'])
def convert(n):
    result={
        "Decimal": n,
        "Binary": binary(n),
        "Octal": octal(n),
        "Hexa Decimal": hexa(n)
    }

    return jsonify(result)


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=3306)