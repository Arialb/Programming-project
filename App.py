from flask import Flask, render_template
from flask import *
from pandas import *
import Operations as Ope

app = Flask('Gene annotation')

f='dataset/Homo_sapiens.GRCh38.85 (3).gff3.gz'
ds=Ope.gff3_databasereader().readata()

#homepage

@app.route('/')
def homepage():
    return render_template('Home.html')
@app.route('/io')
def Ca():
    return render_template('Cards.html')
@app.route('/i')
def home():
    return render_template('Homepage.html')
    
@app.route('/op1')
def op1():
	result=ds.types()
	return render_template("GBI.html",result=result)
@app.route('/op2')
def op2():
	result=ds.unique_sequences()
	return render_template("USI.html",result=result)
@app.route('/op3')
def op3():
	result=ds.unique_types()
	return render_template("UTI.html",result=result)
@app.route('/op4')
def op4():
	result=ds.number_of_features()
	return render_template("NSF.html",result=result)
@app.route('/op5')
def op5():
	result=ds.number_of_entries()
	return render_template("NE.html",result=result)
@app.route('/op6')
def op6():
	result=ds.new_dataset()
	return render_template("NewData.html",result=result)
@app.route('/op7')
def op7():
	result=ds.fraction_of_unassembled_sequences()
	return render_template("Calcolo.html",result=result)
@app.route('/op8')
def op8():
	result=ds.only_entries_from_source()
	return render_template("NewDataOrdrer.html",result=result)
@app.route('/op9')
def op9():
	result=ds.entries_from_each_type()
	return render_template("Count.html",result=result)
@app.route('/op10')
def op10():
	result=ds.gene_names_from_dataset()
	return render_template("Gene.html",result=result)

    

app.run(debug=True)


