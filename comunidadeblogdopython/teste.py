from comunidadeblogdopython import database
from comunidadeblogdopython import app
from comunidadeblogdopython.models import Usuario

# with app.app_context():
#      database.create_all()



# with app.app_context():
#     usuario = Usuario(username="Ademilson", email="ademilson@gmail.com", senha="123456")
#     usuario2 = Usuario(username="Joao", email="joao@gmail.com", senha="123487")
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.commit()

# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo="Primeiro Post", corpo="Nosso primeiro post está de bo")
#     meu_post2 = Post(id_usuario=2, titulo="Primeiro Post", corpo="Nosso primeiro post está de bo")
#     database.session.add(meu_post)
#     database.session.add(meu_post2)
#     database.session.commit()

# with app.app_context():
#     meus_teste = Usuario.query.filter_by(id=3).first()
#     print(meus_teste)
#     print(meus_teste.username)
#     print(meus_teste.email)
#     print(meus_teste.senha)
with app.app_context():
    meus_teste = Usuario.query.all()
    print(meus_teste)





# with app.app_context():
#     meus_post = Post.query.filter_by(id_usuario=1).first()
#    # print(meus_post)
#     print(meus_post.titulo)
#     print(meus_post.autor.username)
#     print(meus_post.corpo)

# with app.app_context():
#     database.drop_all()
#     database.create_all()
