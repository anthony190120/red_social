from database import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    provider = db.Column(db.String(50), default='local')
    foto_perfil = db.Column(db.String(500), default='img/default.jpg')
    banner_imagen = db.Column(db.String(255), default='img/default_banner.gif')
    descripcion = db.Column(db.String(255), nullable=True)
    edad = db.Column(db.Integer, nullable=True)
    centro_educativo = db.Column(db.String(255), nullable=True)
