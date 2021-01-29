# render_template for renedering html files, request for getting values from textfields in webpages
import math

from flask import  Flask,render_template,request,session,redirect,flash
from datetime import datetime
# mysql connector
import mysql.connector
# Importing Json module
import json
# For sending email
import smtplib

# For setting path in uploader route
import os

#For getting files securely
from werkzeug.utils import secure_filename

# Creating a object of smtp
# server = smtplib.SMTP_SSL('smtp.gmail.com',465)
# server.login("senders_email","senders_password")
# server.login("demo.harshit117@gmail.com","demo.harshit")


local_server=True

# Fetchin paramters from json file
with open('config.json','r') as c:
    params=json.load(c)["params"]

if local_server:
    con=mysql.connector.connect(host='localhost',user="harshit",password="123",database=params['local_database'])
else:
    con=mysql.connector.connect(host='localhost',user="harshit",password="123",database=params['prod_database'])

cur = con.cursor()

app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_LOCATION']=params['upload_location']

@app.route("/")
def home():
    # Fetching posts
    cur.execute("select * from posts")
    posts = cur.fetchall()
    # Getting page value
    # This helps us in getting value of argument page in the url
    page = request.args.get('page')
    # Getting value of last
    # print("len fo posts:",len(posts))
    last=math.ceil(len(posts)/int(params['no_of_posts']))
    # print("value of last:",last)
    if not page:
        page=1
    page=int(page)
    # print("value of page : ",page)

    posts=posts[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+int(params['no_of_posts'])]
    if page==1:
        prev="#"
        next="/?page="+str(page+1)
    elif page==last:
        prev='/?page='+str(page-1)
        next='#'
    else:
        prev='/?page='+str(page-1)
        next="/?page="+str(page+1)

    # print("next :",next,"prev :",prev)

    # Pagination Logic
    # First
    # prev =#
    # next = page + 1
    # Middle
    # prev=page-1
    # next=page+1
    # Last
    # prev=prev-1
    # last=#

    # Now er sending our all fetched records to html file index.html
    return  render_template('index.html',params=params,posts=posts,next=next,prev=prev)

@app.route("/about")
def about():
    return render_template('about.html',params=params)

@app.route("/contact",methods =['GET','POST'])
def contact():
    if request.method=="POST":
        # getting data from webpage using request.form.get("field name ")
        sno=11
        name=request.form.get('name')
        phone = request.form.get('phone')
        msg=request.form.get('message')
        date=datetime.now()
        email=request.form.get('email')
        print(name,phone,msg,date,email)

        query = "insert into contacts values('%s','%s','%s','%s','%s','%s')"%(sno,name,phone,msg,date,email)
        try:
            cur.execute(query)
        except Exception as e:
            print(e)
        con.commit()

        # server.sendmail("senders_eamil","recievers_eamil","message")
        # server.sendmail("demo.harshit117@gmail.com", email, name + " has tried contacting you.")

    return render_template(('contact.html'),params=params)


@app.route('/post')
def post():
    return render_template(('post.html'),params=params)

@app.route('/home')
def index():
    return render_template('index.html',params=params)

# <string:post_slug> is like passing a parameter
@app.route('/posts/<string:post_slug>', methods=['GET'])
def post_route(post_slug):

    # Executing query for fetching data from table
    cur.execute("select * from posts where slug='%s'"%(post_slug))
    # Resuxlt will store data in form of tuples
    result = cur.fetchall()
    # post_data has value in tuples
    post_data=result[0]

    # passing data in html file0
    # we can use parameters like {{title}}
    return render_template('post.html',params=params,post=post_data)

@app.route("/edit/<string:sno>",methods =['GET','POST'])
def edit(sno):
    # print(request.method)
    if 'user' in session and session['user'] == params["admin_user"]:
          if request.method=='POST':
              title = request.form.get('title')
              subheading = request.form.get('subheading')
              slug = request.form.get('slug')
              author = request.form.get('author')
              content = request.form.get('content')
              image = request.form.get('image')
              try:
                  query = "update posts set title =%s,subheading=%s,slug=%s,author=%s,content=%s,img_file=%s where sno=%s"
                  val = (title, subheading, slug, author,content, image,sno)
                  cur.execute(query, val)
                  con.commit()
              except Exception as e:
                  print(e)
              return redirect('/edit/'+sno)
          else:
              # print("in get")
              try:
                  cur.execute("select * from posts where sno =%s" % (sno))
                  print(sno)
                  posts=cur.fetchmany(0)
              except Exception as e:
                  print(e)
              return render_template('edit.html',params=params,post=posts[0])


@app.route("/addpost",methods=['GET','POST'])
def addpost():
    if request.method=="POST":

        # For storing image
        f = request.files['image']
        f.save(os.path.join(app.config['UPLOAD_LOCATION'], secure_filename(f.filename)))
        print(f.filename)

        # For storing data in database
        title = request.form.get('title')
        subheading = request.form.get('subheading')
        slug = request.form.get('slug')
        author = request.form.get('author')
        content = request.form.get('content')
        image = f.filename
        try:
            query="insert into posts(title,slug,subheading,author,date,content,img_file) values(%s,%s,%s,%s,%s,%s,%s)"
            val=(title,subheading,slug,author,datetime.now(),content,image)
            cur.execute(query,val)
            con.commit()
        except Exception as e:
            print(e)
        return redirect('/dashboard')

    return render_template('addpost.html',params=params)

@app.route('/dashboard',methods=['POST','GET'])
def login():

    # If any user is already logged in this session than this will return dashboard.html
    if 'user' in session and session['user']==params["admin_user"]:
        cur.execute("select * from posts")
        posts = cur.fetchall()
        return render_template('dashboard.html', params=params, posts=posts)

    # if any user try to log-in then we will return dashboard.html if details are correct/
    if request.method=='POST':
        username=request.form.get('email')
        password=request.form.get('password')
        # print(username,password)
        if username==params['admin_user'] and password==params["admin_password"]:
            session['user'] = username
            cur.execute("select * from posts")
            posts = cur.fetchall()
            return render_template('dashboard.html', params=params,posts=posts)
        else:
            print("unsuccessfull")
    return render_template('login.html',params=params)


@app.route("/uploader",methods=['GET','POST'])
def uploader():
    if ('user' in session and session['user']==params['admin_user']):
        if request.method=='POST':
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_LOCATION'],secure_filename(f.filename)))
            return "Upload Succesfully"

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route('/delete/<string:sno>')
def delete(sno):
    try:
        cur.execute("delete from posts where sno=%s"%(sno))
        con.commit()
    except Exception as e:
        print(e)

    return redirect('/dashboard')

# To run the server
# app.run(host="hostname/host number",port="port number", debug=True)
app.run(debug=True)

con.close()
cur.close()
