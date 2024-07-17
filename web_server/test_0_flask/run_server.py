from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/register',methods=['GET'])
def register():
    return render_template('register.html')
    
#使用get方法提交数据        
# @app.route('/do_register',methods=['GET'])
# def do_register():
#     print(request.args)
#     return render_template('do_register.html')

#使用post方法提交数据
@app.route('/do_register',methods=['POST'])
def do_register():
    #返回的表单是一个类似字典的列表
    print(request.form)
    #根据键名获取对应的值
    user_name = request.form.get("user_name")
    pwd = request.form.get("pwd")
    #获取多个值用request.form.getlist()
    # hobby = request.form.getlist(hobby)
    print(user_name,pwd)
    return render_template('do_register.html')


if __name__ == '__main__':
    app.run(debug=True)