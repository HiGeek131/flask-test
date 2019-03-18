from flask import Flask, render_template, request
import pymysql


app = Flask(__name__)


def sql_init():
    db = pymysql.connect('127.0.0.1', 'user_name', 'password', 'user_DB')
    cursor = db.cursor()
    sql = """create table if not exists test_web_data(
                    name varchar(20),
                    password varchar(20))"""
    cursor.execute(sql)
    db.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test', methods=['POST'])
def success():
    if request.method == 'POST':
        user_name = request.form['name']
        user_password = request.form['pass']
        sql = "insert into test_web_data values('%s','%s')" % (user_name, user_password)
        db = pymysql.connect('127.0.0.1', 'user_name', 'password', 'user_DB')
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
            # print('sql insert success!')
        except:
            db.rollback()
            # print('sql insert error!')
        db.close()
        return render_template('success.html', name=user_name)
    else:
        pass


if __name__ == '__main__':
    sql_init()
    app.run(host='0.0.0.0', port=80)
