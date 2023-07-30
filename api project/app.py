from flask import Flask,render_template,request
import requests 

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if request.method=='POST':
        num:int=request.form['input']
        choice=request.form['choice']

        data=requests.get(f"https://arijitghosh.pythonanywhere.com/convert/{num}")
        data=data.json()

        if choice=='bin':
            mode="Binary"
            ans=data['Binary']
        elif choice=='oct':
            mode="Octal"
            ans=data['Octal']
        elif choice=='hex':
            mode="Hexa Decimal"
            ans=data['Hexa Decimal']
        else:
            ans="No option selected"
        
        # print(ans)
        return render_template("index.html",ans=ans,dec=num,mode=mode)

    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0") 