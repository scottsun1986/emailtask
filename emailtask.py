from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from  flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,validators

app= Flask(__name__)
app.config['SECRET_KEY']='HARD'
bootstrap=Bootstrap(app)


class NameForm(FlaskForm):
    name=StringField("姓名：",[validators.Length(min=4, max=25,message="只能在4个字到25个字之间")])
    submit=SubmitField("提交")

@app.route("/",methods=['GET','POST'])
def index():
    name=None
    form=NameForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
    return render_template("index.html",form=form,name=name)

if __name__ == '__main__':
    app.run(debug=True)
