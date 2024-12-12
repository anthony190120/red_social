from flask import Flask, redirect, url_for
from routes.auth import auth_bp
from routes.usuario import usuario_bp
from config import Config
from database import db  # Importa la instancia única de db
from flask_migrate import Migrate   

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)  # Inicializa db con la app

    # Inicializar Flask-Migrate
    migrate = Migrate(app, db)

    # Registrar blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(usuario_bp, url_prefix='/usuario')
    
    @app.route('/')
    def home():
        return redirect(url_for('auth_bp.login'))
    
    return app

app = create_app()  # Crear la instancia de la aplicación

if __name__ == '__main__':
    app.run(debug=True)
