from flask import Flask,render_template,request,redirect,url_for,session,flash



import sqlite3
import os
con=sqlite3.connect("reg.db")
con.execute("create table if not exists regester(pid integer,name text,email text,password text)")
con.close()


app= Flask(__name__) 
app.secret_key="1409"





@app.route('/index')
def home(): 
    
    
    return render_template('index.html')
@app.route('/login',methods=['POST','GET'])

def product(): 
    if request.method=='POST':
        name=request.form['lname']
        password=request.form['lpassword']
        con=sqlite3.connect("reg.db")
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("select * from regester where name=? and password=?",(name,password))
        data=cur.fetchone()

        if data:
            session["name"]=data["name"]
            session["password"]=data["password"]
            return redirect("dash")
        else:
            flash("username and password mismatch","danger")

    
    return render_template('login.html')

@app.route('/reg',methods=['POST','GET'])
def reg(): 
    if request.method=='POST':
        try:
            name=request.form['name']
            email=request.form['email']
            password=request.form['password']
            con=sqlite3.connect("reg.db")
            cur=con.cursor()
            cur.execute("insert into regester(name,email,password)values(?,?,?)",(name,email,password))
            con.commit()
            

        except:
            flash("eror in opration","danger")


        finally:
            return redirect("login")
            con.close()
               
                 

    return render_template('regester.html')


@app.route('/dash')


def add_user(): 
    return render_template("dashboard.html")


@app.route('/logout')
def logout(): 
    session.clear()
    flash("You have been logged out!")
    return redirect("login")


@app.route('/question')

def question(): 
   
    return render_template("question.html")

@app.route('/logo')

def logo(): 
   
    return render_template("logo.html")

@app.route('/score')

def score(): 
   
    return render_template("score.html")






if __name__=="__main__":
    app.run(debug=True)
