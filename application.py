from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/staticfiles')
def staticfiles():
    return render_template('staticfiles.html')



@FAI.route('/virat')
def virat():
    return render_template('virat.html')

if __name__=='__main__':
    FAI.run(debug=True)

