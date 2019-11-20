from flask import Flask,redirect,url_for,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project_database import Register,Base

engine = create_engine('sqlite:///bvc.db', connect_args={'check_same_thread': False},echo=True)
Base.metadata.bind=engine

DBSession=sessionmaker(bind=engine)
session=DBSession()

app=Flask('__name__')

@app.route("/name")
def hello():
	return "Hello welcome pawan lamichhane"

@app.route("/harish")
def Babu():
	return "My name is Harish and I am BVCian"

@app.route("/data/<name>")
def data(name):
	name = "Hari"
	return "HELLO! {}".format(name)

@app.route("/<name>/<roll>")
def xyz(name,roll):
	name = 'Harish'
	rollno = '5B7'
	return "My name is{} and rollno is{}".format(name,roll)

@app.route("/admin")
def admin():
	return render_template("sample.html")

@app.route("/student")
def student():
	return "<font color = 'red'>hello welome to student page"

@app.route("/faculty")
def faculty():
	return "welcome to faculty data"

@app.route("/person/<unname>")
def person(unname):
	return render_template("sample1.html", name=unname)

@app.route("/table/<int:num>")
def table(num):
	return render_template("table.html", n=num)




@app.route("/user/<name>")
def user(name):
	if name == 'faculty':
		return redirect(url_for('faculty'))
	elif name=='student':
		return redirect(url_for('student'))
	elif name=='admin':
		return redirect(url_for('admin'))
	else:
		return "url not found"


dummy_data=[{'name':'Hari','org':'BVC','DOB': '24 nov 2000'},
				{'name':'pawan','org':'BVCEC','DOB': '30 dec 2000'}]
@app.route("/show")
def data_show():
	return render_template("show_data.html", d=dummy_data)

@app.route("/register")
def reg():
	return render_template('sample2.html')

@app.route("/file")
def file_upload():
	return render_template("upload.html")


@app.route("/success", methods =["POST","GET"])
def success():
	if request.method == "POST":
		f = request.files["file"]
		f.save(f.filename)
		return render_template("display.html", name = f.filename)

@app.route("/show_data")
def showData():
	register=session.query(Register).all()
	return render_template('show.html', register=register)

@app.route("/add",methods=["POST","GET"])
def addData():

	if request.method=="POST":
		newData=Register(name=request.form['name'],surname=request.form['surname'],
			regd_no=request.form['regd_no'],mobile=request.form['mobile'],
			branch=request.form['branch'],email=request.form['email'])
		session.add(newData)
		session.commit()
		return redirect(url_for('showData'))
	else:
		return render_template('new.html')

@app.route('/<int:register_id>/edit',methods=["POST","GET"])
def editData(register_id):
	editedData=session.query(Register).filter_by(id=register_id).one()
	if request.method=="POST":
		editedData.name=request.form['name']
		editedData.surname=request.form['surname']
		editedData.regd_no=request.form['regd_no']
		editedData.mobile=request.form['mobile']
		editedData.branch=request.form['branch']
		editedData.email=request.form['email']
		session.add(editedData)
		session.commit()
		return redirect(url_for('showData'))
	else:
		return render_template('edit.html',register=editedData)

@app.route('/<int:register_id>/delete',methods=["POST","GET"])
def deleteData(register_id):
	deletedData=session.query(Register).filter_by(id=register_id).one()

	if request.method=="POST":
		session.delete(deletedData)
		session.commit()
		return redirect(url_for('showData',register_id=register_id))

	else:
		return render_template('delete.html',register=deletedData)


if __name__=='__main__':
	app.run(debug=True)
