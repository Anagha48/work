from flask import Flask,request,render_template,redirect,url_for,make_response
from mydatabase import MyDatabase
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def displayform():
    if request.method=='GET':
        return render_template("form.html")
    else:
        # FETCH THE FORM DETAILS
        title=request.form['title']
        description=request.form['desc']
        date=request.form['date']
        print(title,description,date)
        
        mydb=MyDatabase()
        sql=f"insert into mybook(title,description,date)values('{title}','{description}','{date}')"
        mydb.insert(sql)
        return render_template('form.html',msg="data stored suuccessfully")
    
@app.route('/view',methods=['GET','POST'])
def view():
    mydb = MyDatabase()
    data = mydb.view()
    print(data)
    return render_template('formview.html',data=data)

@app.route('/edit/<id>',methods=['GET','POST'])
def edit(id):
    print(id)
    if request.method=='GET':
        mydb = MyDatabase()
        sql = "select * from mybook where id='"+id+"'"
        data = mydb.selectone(sql)
        print(data)
        return render_template("edit.html",data=data)
    else:
        title = request.form['title']
        description = request.form['desc']
        date = request.form['date']
        print(title,description,date)
        mydb = MyDatabase()
        sql = 'update mybook set title="'+title+'",description="'+description+'",date="'+date+'"where id="'+id+'"'
        mydb.update(sql)
        return redirect(url_for('view'))

@app.route('/del/<id>',methods=['GET','POST'])
def delete(id):
    print(id)
    mydb =  MyDatabase()
    sql = 'DELETE FROM mybook WHERE id="'+id+'"'
    mydb.delete(sql)
    return redirect(url_for('view'))

if __name__=='__main__':
    app.run(debug=True)
