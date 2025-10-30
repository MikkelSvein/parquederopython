Parqueadero La 64 - Django scaffold
----------------------------------
Instrucciones rápidas:

1. Crear un virtualenv y activar:
   python3 -m venv venv
   source venv/bin/activate   (Windows: venv\Scripts\activate)

2. Instalar requerimientos:
   pip install -r requirements.txt

3. Migrar y crear superuser:
   python manage.py migrate
   python manage.py createsuperuser

4. Ejecutar servidor:
   python manage.py runserver

Notas:
- Usuario modelo extendido en app 'usuarios' (User).
- Tarifa: se crea una fila por defecto desde admin o migraciones manuales.
