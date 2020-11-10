from flask import Flask,render_template,redirect,request,url_for
import math
app=Flask(__name__)
@app.route("/")
@app.route('/<int:num>')
def inputTest(num=None):
    return render_template('main.html',num=num)
    
@app.route('/calculate',methods=['POST','GET'])
def calculate(num=None):
    if request.method=='POST':
        temp=request.form['num']
    elif request.method=='GET':
        temp=request.args.get('num')
    temp = int(temp)
    while temp%2==0:
        max_Prime=2
        temp/=1
    for i in range(3,int(math.sqrt(temp))+1,2):
        while temp % i == 0 :
            max_Prime=i
            temp=temp/i
    if temp>2:
        max_Prime=temp
    return redirect(url_for('inputTest',num=max_Prime))
if __name__=='__main__':
    app.run('0.0.0.0',port=8080,debug=True)
