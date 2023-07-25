from flask import Flask,render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configure the Extension
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todolists.db"
db.init_app(app)


# Define Models
class Todo(db.Model):
    sl = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime, default = datetime.now())

    def __repr__(self) -> str:
        return f"{self.sl} - {self.title}"

with app.app_context():
    db.create_all()

@app.route("/",methods=['GET','POST'])
def index():

    if request.method== "POST":
        title=request.form['title']
        subject=request.form['subject']
        todo=Todo(title=title,subject=subject)
        db.session.add(todo)
        db.session.commit()

    # query data
    allTodo=Todo.query.all() #v2.0.x
    # track=len(list(allTodo))

    return render_template("index.html",alllist=allTodo)

@app.route("/delete/<int:serial>")
def delete(serial):
    item= db.session.execute(db.select(Todo).filter_by(sl=serial)).scalar_one()
    db.session.delete(item)
    db.session.commit()
    return redirect('/')

@app.route("/update/<int:serial>",methods=['GET','POST'])
def update(serial):
    if request.method=="POST":
        title=request.form['title']
        subject=request.form['subject']
        item=db.session.execute(db.select(Todo).filter_by(sl=serial)).scalar_one()
        item.title=title
        item.subject=subject
        db.session.add(item)
        db.session.commit()

        return redirect("/")

    item= db.session.execute(db.select(Todo).filter_by(sl=serial)).scalar_one()
    return render_template("update.html",item=item)

if __name__=="__main__":
    app.run(debug=True)