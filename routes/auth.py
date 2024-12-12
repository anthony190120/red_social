from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app as app
from werkzeug.utils import secure_filename
from database.models import Usuario, db
from werkzeug.security import generate_password_hash, check_password_hash
import os
import posixpath  # Importamos posixpath para usar '/' en las rutas

auth_bp = Blueprint('auth_bp', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@auth_bp.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if 'usuario_id' not in session:
        return redirect(url_for('auth_bp.login'))

    usuario = Usuario.query.get(session['usuario_id'])
    if request.method == 'POST':
        if 'foto_perfil' in request.files:
            file = request.files['foto_perfil']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # Usamos posixpath para asegurar que el separador sea '/'
                usuario.foto_perfil = posixpath.join('img', filename)
        
        if 'banner_imagen' in request.files:
            file = request.files['banner_imagen']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                usuario.banner_imagen = posixpath.join('img', filename)
        
        db.session.commit()
        flash('Perfil actualizado.', 'success')

    return render_template('perfil.html', usuario=usuario)



@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']
        usuario = Usuario.query.filter_by(correo=correo).first()
        
        if usuario and check_password_hash(usuario.password, password):
            session['usuario_id'] = usuario.id
            flash('Has iniciado sesión.', 'success')
            return redirect(url_for('usuario_bp.perfil'))
        else:
            flash('Correo o contraseña incorrectos.', 'error')
            return redirect(url_for('auth_bp.login'))
    
    return render_template('auth.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        password = request.form['password']
        
        usuario_existente = Usuario.query.filter_by(correo=correo).first()
        if usuario_existente:
            flash('El correo ya está registrado.', 'error')
            return redirect(url_for('auth_bp.register'))
        
        password_hash = generate_password_hash(password)
        nuevo_usuario = Usuario(nombre=nombre, correo=correo, password=password_hash)
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        flash('Registro exitoso. Por favor, inicia sesión.', 'success')
        return redirect(url_for('auth_bp.login'))
    
    return render_template('auth.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión.', 'success')
    return redirect(url_for('auth_bp.login'))
