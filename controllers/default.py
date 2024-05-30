from flask import render_template, request, redirect, flash
from run import app, db
from models.tabelas import Tarefa

@app.route('/')
def index():
    lista_tarefas = Tarefa.query.all()
    return render_template('index.html', lista_tarefas = lista_tarefas)


# CRUD DO GERENDICADOR DE TAREFA.
@app.route('/criar', methods=['POST'])
def criar():
    titulo = request.form['titulo']
    data_realizacao = request.form['data-realizacao']
    descricao = request.form['descricao']
    tarefa = Tarefa(titulo=titulo, data_realizacao=data_realizacao, descricao=descricao)
    db.session.add(tarefa)
    db.session.commit()
    return redirect('/')

@app.route('/editar/<int:id>')
def editar(id):
    tarefa = Tarefa.query.filter_by(id=id).first()
    return render_template('editar.html', tarefa = tarefa)

@app.route('/atualizar', methods=['POST'])
def atualizar():
    tarefa = Tarefa.query.filter_by(id=request.form['id']).first()
    tarefa.titulo = request.form['titulo']
    tarefa.data_realizacao = request.form['data-realizacao']
    tarefa.descricao = request.form['descricao']
    db.session.add(tarefa)
    db.session.commit()
    flash('Atualizada com sucesso!')
    return redirect('/')

@app.route('/deletar/<int:id>')
def deletar(id):
    Tarefa.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Deletado com sucesso!!!')
    return redirect('/')
# FIM DO CRUD.