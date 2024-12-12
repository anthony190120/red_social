from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database.models import Usuario, db

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if 'usuario_id' not in session:
        flash('Por favor, inicia sesión.', 'error')
        return redirect(url_for('auth_bp.login'))
    
    usuario_id = session['usuario_id']
    usuario = Usuario.query.get(usuario_id)
    
    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.correo = request.form['correo']
        db.session.commit()
        flash('Perfil actualizado correctamente.', 'success')
        return redirect(url_for('usuario_bp.perfil'))
    
    return render_template('perfil.html', usuario=usuario)
