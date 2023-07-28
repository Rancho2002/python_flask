from flask import Flask,render_template,request
import random 

app = Flask(__name__)



@app.route("/",methods=['GET','POST'])
def home():
    if request.method=='POST':
        text:str=request.form['input']
        choice=request.form['choice']
        if choice=='reverse':
            text=list(text)
            text.reverse()
            ans=''.join(text)
        elif choice=='upper':
            ans=text.upper()
        elif choice=='lower':
            ans=text.lower()
        elif choice=='sentence':
            ans=text.capitalize()
        elif choice=='length':
            ans=len(text)
        elif choice=='swapcase':
            ans=text.swapcase()
        
        elif choice=="jumble":
            text=random.sample(text, len(text))
            ans=''.join(text)

        elif choice=="makeArr":
            ans=list(text)
            ans=[i for i in ans if i!=" "]
            
        else:
            ans="invalid choice selected"
        return render_template("index.html",ans=ans)

    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0") 