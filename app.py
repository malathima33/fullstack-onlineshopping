from flask import Flask,render_template,url_for,request,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'shopping'
 
mysql = MySQL(app)





@app.route('/')
def home():
    return render_template('index.html')


@app.route('/indexpage',methods=['GET','POST'])
def indexpageredirect():
    if request.method == 'POST':
        getinput = request.form['Submit']
        if getinput == 'register':
            return render_template('register.html')
        elif getinput == 'login':
            return render_template('login page.html')


@app.route('/register',methods=['GET','POST'])
def customer():
    if request.method == 'POST':
        try:
            name = request.form['firstname']
            age = request.form['age']
            dist = request.form['opt']
            quali = request.form['qual']
            mob = request.form['contact']
            pasword = request.form['pwd']
            print(name)
            print(age)
            print(dist)
            print(quali)
            print(mob)
            print(pasword)
            cursor = mysql.connection.cursor()
            cursor.execute(''' INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s)''',(name,age,dist,quali,mob,pasword))
            mysql.connection.commit()
            cursor.close()
            return 'successfully stored...!'
        except Exception as e:
            print(e)
    return 'something wrong'



@app.route('/loginpage',methods=['GET','POST'])
def userlogin():
    if request.method=='POST':
        name = request.form['name']
        pwd = request.form['pwd']
        print(name)
        print(pwd)
        cursor = mysql.connection.cursor()
        value = cursor.execute('''select * from customer where(name=%s and password=%s)''',(name,pwd))
        if value!=0:
            return 'user found'
        else:
            return 'incorrect user name and password'







if __name__ =='__main__':
    app.run(debug=True)