from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # Usando SQLite para começar
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo da Tarefa
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.Boolean, default=False)  # False = Pendente, True = Concluída

# Garantir que o create_all seja executado no contexto correto
with app.app_context():
    db.create_all()

# Rota para exibir a página principal e listar as tarefas
@app.route('/')
def index():
    tasks = Task.query.all()  # Obtém todas as tarefas
    return render_template('index.html', tasks=tasks)

# Rota para adicionar uma nova tarefa
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    if title:
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))


# Rota para alternar o status da tarefa (Concluída/Pendente)
@app.route('/update/<int:task_id>')
def update_task(task_id):
    task = Task.query.get(task_id)
    task.status = not task.status  # Alterna entre concluída/pendente
    db.session.commit()
    return redirect(url_for('index'))

# Rota para excluir uma tarefa
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
