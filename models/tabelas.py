from run import db

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(50), nullable=False)
    data_realizacao = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return self._titulo
