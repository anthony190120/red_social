document.addEventListener('DOMContentLoaded', function() {
    const editBtn = document.getElementById('edit-profile-btn');
    const editForm = document.getElementById('edit-profile-form');
  
    editBtn.addEventListener('click', function() {
      if (editForm.style.display === 'block') {
        editForm.style.display = 'none';
      } else {
        editForm.style.display = 'block';
        // Desplazarse hacia el formulario
        editForm.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });
  