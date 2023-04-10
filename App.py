from flask import Flask, render_template
from flask import *
import Operations as Ope

app = Flask('Gene annotation')

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
	return render_template("Types.html",result=result)
@app.route('/op2')
def op2():
	result=ds.unique_sequences()
	return render_template("UniqueSeq.html",result=result)
@app.route('/op3')
def op3():
	result=ds.unique_types()
	return render_template("UniqueTypes.html",result=result)
@app.route('/op4')
def op4():
	result=ds.number_of_features()
	return render_template("NumberFeatures.html",result=result)
@app.route('/op5')
def op5():
	result=ds.number_of_entries()
	return render_template("NumberEntries.html",result=result)
@app.route('/op6')
def op6():
	result=ds.new_dataset()
	return render_template("NewDataset.html",result=result)
@app.route('/op7')
def op7():
	result=ds.fraction_of_unassembled_sequences()
	return render_template("UnassembledSeq.html",result=result)
@app.route('/op8')
def op8():
	result=ds.only_entries_from_source()
	return render_template("EntrySource.html",result=result)
@app.route('/op9')
def op9():
	result=ds.entries_from_each_type()
	return render_template("EntryType.html",result=result)
@app.route('/op10')
def op10():
	result=ds.gene_names_from_dataset()
	return render_template("GeneData.html",result=result)
    

app.run(debug=True)


