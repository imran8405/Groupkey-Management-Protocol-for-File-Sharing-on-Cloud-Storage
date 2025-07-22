from flask import Flask,render_template,request,session,redirect,url_for
import mysql.connector


import pandas as pd

db=mysql.connector.connect(user="root",port=3306,database="System",charset="utf8")
cur=db.cursor()

app=Flask(__name__)
app.config['SECRET_KEY']='Secure project'


@app.route('/')
def index():
    return render_template('ind.html')

@app.route('/start')
def start():
    return render_template('start.html')



@app.route('/cloudprovider',methods=['POST','GET'])
def cloudprovider():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        print("123456789")
        if email == 'cloud@gmail.com' and password == '1234':
            msg = "Cloud Service Provider Login Successfull"
            print('hello')
            return render_template('csphome.html',msg=msg)
        msg = "Provide valid credentials"
        return render_template('start.html',msg=msg)
    return render_template('start.html')



@app.route('/addgroup',methods=['POST','GET'])
def addgroup():
    if request.method=='POST':
        name=request.form['groupname']
        type=request.form['grouptype']
        description=request.form['groupdescription']
        sql="insert into groups(groupname,grouptype,groupdescription) values (%s,%s,%s)"
        values=(name,type,description)
        cur.execute(sql,values)
        db.commit()
        msg="Group Created successfully"
        return render_template('addgroup.html',msg=msg)
    return render_template('addgroup.html')


@app.route('/viewgroups')
def viewgroups():
    sql="select * from groups"
    data=pd.read_sql_query(sql,db)
    print(data)
    return render_template('viewgroup.html',cols=data.columns.values,data=data.values.tolist())


@app.route('/reqaccept/<r>')
def reqaccept(r=0):
    sql="update ureg set status='Accepted' where status='pending' and slno=%s " %(r)
    cur.execute(sql)
    db.commit()
    return redirect(url_for('userreq'))


@app.route('/allusers')
def allusers():
    sql="select slno,name,email,number from ureg where status='Accepted'"
    data=pd.read_sql_query(sql,db)
    db.commit()
    return render_template('allusers.html',cols=data.columns.values,data=data.values.tolist())



@app.route('/registration',methods=['POST','GET'])
def registration():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        contact=request.form['number']
        password=request.form['password']
        conpass=request.form['conpass']
        if password == conpass:
           sql="insert into ureg(name,email,number,password) values (%s,%s,%s,%s)"
           values=(name,email,contact,password)
           cur.execute(sql,values)
           db.commit()
           msg="Registered successfully"
           return render_template('login.html',msg=msg)
        msg='Invalid Credentials'
        return render_template('registration.html',msg=msg)
    return render_template('registration.html')

@app.route('/login',methods=['POST','GET'])
def login():
    print('hello')
    if request.method=='POST':
        email=request.form['email']
        session['email']=email
        password=request.form['password']
        sql = "select * from ureg where status='Accepted'"
        cur.execute(sql)
        data = cur.fetchall()
        db.commit()
        for i in data:
            print(i)
            try:
                if email in i[2] and password in i[4]:

                    return render_template('userhome.html')
            except:
                return render_template('login.html')
        msg="Your registration is not accepted or invalid details"
        return render_template('login.html',msg=msg)
    return render_template('login.html')

@app.route('/userreq')
def userreq():
    sql="select slno,name,email,number,status from ureg where status='pending'"
    data = pd.read_sql_query(sql, db)
    print(data)
    return render_template('userreq.html',cols=data.columns.values,data=data.values.tolist())

@app.route('/group')
def group():
    sql="select id,groupname,grouptype,groupdescription,members from groups"
    data=pd.read_sql_query(sql,db)
    db.commit()
    print(data)
    return render_template('viewgroups.html',cols=data.columns.values,data=data.values.tolist())

@app.route('/joining/<a>/<b>/<c>/<d>')
def joining(a=0,b="",c="",d=""):
    print(b,c)
    sql = "select * from addgroup where Groupname='%s' and  email='%s'"%(b,session['email'])
    cur.execute(sql)
    data = cur.fetchall()
    if data ==[]:
        sql="insert into addgroup (groupname,grouptype,groupdescription,email) values('%s','%s','%s','%s')"%(b,c,d,session['email'])
        cur.execute(sql)
        db.commit()
        sql="select * from groups where groupname='%s' "%(b)
        cur.execute(sql)
        data=cur.fetchall()
        print("===",data,"===")
        if data!=[]:
            sql = "select count(*) from addgroup where Groupname='%s' and  email='%s'"%(b,session['email'])
            cur.execute(sql)
            data = cur.fetchall()
            count=data[0][0]
            # members=data[0][1]
            print(count,"ABCDEFGHI")
            sql="select count(*) from addgroup where groupname='%s'"%(b)
            cur.execute(sql)
            dat = cur.fetchall()
            print(dat)
            count = dat[0][0]
            sql="update groups set members='%s' where groupname='%s'"%(count,b)
            cur.execute(sql)
            db.commit()
           
        else:
            pass
    else:
        print("you are already a member of this Group")
    return redirect(url_for('group'))

@app.route('/vmg')
def vmg():
    sql="select groupname,grouptype,groupdescription,members from groups "
    data=pd.read_sql_query(sql,db)
    db.commit()
    return render_template('vmg.html',cols=data.columns.values,data=data.values.tolist())


@app.route('/uploadfiles',methods=['POST','GET'])
def uploadfiles():
    if request.method=='POST':
        f = request.form['filename']
        file = request.files['file']
        x = file.read().decode('UTF-8')
        email=session['email']
        print(x)
        # sql="insert into filesa (filename,file,email) values (%s,%s,AES_ENCRYPT(%s,'rupesh'))"
        sql="insert into filesa (filename,email,file) values (%s,%s,AES_ENCRYPT(%s,'rupesh'))"
        val=(f,session['email'],x)
        cur.execute(sql,val)
        db.commit()
        msg="file uploaded successfully"
        return render_template('uploadfile.html',msg=msg)
    return render_template('uploadfile.html')

@app.route('/myfiles')
def myfiles():
    sql="select filename from filesa where email='%s'"%(session['email'])
    data=pd.read_sql_query(sql,db)
    db.commit()
    return render_template('myfiles.html',cols=data.columns.values,data=data.values.tolist())


@app.route('/viewfiles/<x>')
def viewfiles(x=""):
    sql="select file from filesa where email='%s' and filename='%s'"%(session['email'],x)
    data=pd.read_sql_query(sql,db)
    db.commit()
    msg=data
    return render_template('viewfiles.html',msg=msg)


@app.route('/g/<f>')
def g(f=""):
    print(f)
    sql="select file from filesa where email='%s'"%(session['email'])
    cur.execute(sql)
    data=cur.fetchall()
    db.commit()
    print(data[0][0])
    session['data']=data[0][0]

    sql="select groupname,grouptype,groupdescription,email from groups"
    data=pd.read_sql_query(sql,db)
    db.commit()
    return render_template('g.html',x=f,cols=data.columns.values,data=data.values.tolist())


@app.route('/s/<m>')
def s(m=""):
    print(m)
    print(session['data'])
    sql="update groups set file=%s where groupname=%s "
    val=(session['data'],m)
    cur.execute(sql,val)
    db.commit()
    # sql = "select * from filesa where email=%s" % (session['email'])
    # cur.execute(sql)
    # data = cur.fetchall()
    # db.commit()
    # print(data)
    return render_template('s.html',msg=m)


@app.route('/sendmessage',methods=['POST','GET'])
def sendmessage():
    if request.method=='POST':
        msg=request.form['message']
        sql = "update filesa set message=%s where email=%s"
        values = (msg, session['email'])
        cur.execute(sql, values)
        db.commit()
    return render_template('msg.html')


@app.route('/timeline')
def timeline():
    # sql="SELECT Orders.OrderID, Customers.CustomerName FROM Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID"
    # sql="SELECT filesa.email,filesa.filename,groups.groupname,filesa.message FROM filesa inner join groups ON filesa.email = groups.email;"
    sql="select filename,message,email from filesa"
    data=pd.read_sql_query(sql,db)
    db.commit()
    print(data)
    return render_template('timeline.html',cols=data.columns.values,data=data.values.tolist())


@app.route('/showfiles/<z>/<v>')
def showfiles(z="",v=""):
    print(z)
    print(v)
    sql = "select AES_DECRYPT(file, 'rupesh')decrypt from filesa where filename='%s' "%(z)
    cur.execute(sql)
    data = cur.fetchall()
    print(data[0][0])
    data = data[0][0].decode('UTF8')
    db.commit()
    print(data)
    msg=data
    return render_template('showfile.html',msg=msg)


if __name__=='__main__':
    app.run(debug=True)