from main import app, database
from models import Usuario, Post

# with app.app_context():
#     database.create_all()



# with app.app_context():
#     usuario = Usuario(username="Ademilson", email="ademilson@gmail.com", senha="123456")
#     usuario2 = Usuario(username="Joao", email="joao@gmail.com", senha="123487")
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.commit()

with app.app_context():
    meus_usuarios = Usuario.query.all()
    print(meus_usuarios)
