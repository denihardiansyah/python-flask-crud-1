from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://deni:Arc3lon2020@rm-d9j68ze953q6449rpxo.pgsql.ap-southeast-5.rds.aliyuncs.com:3433/mydb'
=======
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://deni@localhost:5432/mydb
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://deni:Arc3lon2020@rm-d9j68ze953q6449rp.pgsql.ap-southeast-5.rds.aliyuncs.com:3433/mydb'
>>>>>>> 920ae1ea0dc3723e6ba43c842669907067ae2a45
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
  __tablename__ = 'todos'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(), nullable=False)
  completed = db.Column(db.Boolean(), nullable=False, default=False)

  def __repr__(self):
    return f'<Todo {self.id} {self.description}>'

#db.create_all()

@app.route('/todos/create', methods=["POST"])
def create_todo():
  error = False
  body = {}
  try:
    description = request.get_json()['description']
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    body['description'] = todo.description
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()
  if not error:
    return jsonify(body)
  

@app.route('/')
def index():
  return render_template('index.html', data=Todo.query.all())
