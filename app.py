import pymongo
from flask import Flask, render_template, jsonify, request, Response

client = pymongo.MongoClient(
    "mongodb+srv://Abner:Abner666@virus2.a6ehgde.mongodb.net/?retryWrites=true&w=majority")
db = client['UAP']

result = db.Info
print(result)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index4.html',)


List1 = []
List2 = []


@app.route('/score', methods=['POST'])
def get_score():
    global List1  # 声明为全局变量
    data = request.get_json()  # 获取前端发送的JSON数据

    # 在这里处理接收到的数据
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    password = data['password']
    class_selection = data['class']

    # 进行其他逻辑处理...
    List1 = [first_name, last_name, email, password, class_selection]
    print(List1)
    return {'message': 'Score received successfully 1'}


@app.route('/score2', methods=['POST'])
def get_score2():
    global List2  # 声明为全局变量
    data = request.get_json()  # 获取前端发送的JSON数据

    # 在这里处理接收到的数据
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    password = data['password']
    class_selection = data['class']

    # 进行其他逻辑处理...
    List2 = [first_name, last_name, email, password, class_selection]
    print(List2)

    if List1 == List2:
        print('Yes')

        # 查询数据库中是否存在相同数据
        query = {
            'firstName': first_name,
            'lastName': last_name,
            'email': email,
            'password': password,
            'class': class_selection
        }
        existing_data = result.find_one(query)

        if existing_data:
            print('Data already exists in the database')
            return {'message': 'Data already exists'}  # 返回一个有效的响应
        else:
            print('Data does not exist in the database, performing insertion')

            # 插入数据到MongoDB
            document = {
                'firstName': first_name,
                'lastName': last_name,
                'email': email,
                'password': password,
                'class': class_selection
            }
            result.insert_one(document)

            return {'message': 'Data inserted successfully'}  # 返回一个有效的响应

    else:
        print('No')
        return {'message': 'No'}  # 返回一个有效的响应


if __name__ == '__main__':
    app.run()
