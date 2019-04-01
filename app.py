from flask import Flask,render_template,request
import os
from database import Database
from utils import genrate_number

app=Flask(__name__) #flask object

@app.route('/') #home page address
def index(): #function that will run when home page
    return render_template('index.html')


@app.route('/home')  # home page address
def home():  # function that will run when home page
    return render_template('home.html')


@app.route('/results')  # home page address
def results():  # function that will run when home page
    numbers= genrate_number(100)
    return render_template('results.html',nums=numbers,page_name='results')




@app.route('/expense', methods=['GET','POST'])  # home page address
def expense():  # function that will run when home page
    msg=''
    if request.method=='POST':
        item=request.form.get('item')
        price=request.form.get('price')
        print(item,price)
        db=Database()
        db.create_table()
        status=db.add(item,price)
        if status:
            msg='saved'
        else:
            msg='not saved'
    results = Database().view()
    return render_template('expenseform.html',msg=msg,results=results)
    
if __name__ == "__main__":
    app.run(debug=True) #starts the webserver when run app.py
