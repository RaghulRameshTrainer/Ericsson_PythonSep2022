from flask import Flask,request,jsonify,make_response
from flask_restful import Resource,Api
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

employee=[
    {
        'name':'Raghul Ramesh',
        'tech':[
            {
                'name':'Python',
                'exp':18
            }
        ]
    },
    {
        'name':'Malini',
        'tech':[
            {
                'name':'Java',
                'exp':15
            }
        ]
    }
]

@app.route('/emp/<string:name>')
def get_employee(name):
    for data in employee:
        if(data['name']==name):
            return jsonify({'Found:' : data['name']})
    return jsonify({'message':'employee not found'})

@app.route('/emp/<string:name>/tech')
def get_tech(name):
    for data in employee:
        if(data['name']==name):
            return jsonify(data['tech'])
    return jsonify({'message': 'employee not found'})

@app.route('/emp',methods=['POST'])
def add_employee():
    emp_data=request.get_json()
    new_emp={
        'name':emp_data['name'],
        'tech':[]
    }
    employee.append(new_emp)
    return jsonify(new_emp)

@app.route('/emp/<string:name>/tech',methods=['POST'])
def add_employee_info(name):
    for data in employee:
        if(data['name']==name):
            emp_data = request.get_json()
            new_tech={
                'name':emp_data['name'],
                'exp':emp_data['exp']
            }
            #data['name'].append(new_tech)
            return jsonify(new_tech)
    return jsonify({'message': 'employee not found'})


@app.route('/emp_update/<string:name>/tech',methods=['PUT'])
def update_employee_info(name):
    for data in employee:
        if(data['name']==name):
            emp_data = request.get_json()
            new_tech={
                'exp':emp_data['exp']
            }
            #data['name'].append(new_tech)
            return jsonify(new_tech)
    return jsonify({'message': 'employee not found'})



@app.route('/')
def home():
    return "Hello Everyone!"

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s' % name

@app.route('/hello/<int:empid>')
def show_empinfo(empid):
    return 'EMP ID : %d' % empid
if __name__=='__main__':
    app.run(port=8000)