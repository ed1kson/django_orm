import django_setup
from modules.models import User, Category, Product, Game, Genre

def add_user(name, email):
    User(
        name = name,
        email = email,
        role = 'user'
    ).save()

def add_admin(name, email):
    User(
        name = name,
        email = email,
        role = 'admin'
    ).save()

def delete_user_by_email(email):
    chmo = User.objects.get(email = email)
    chmo.delete()

def update_users_data(id, name = None, email = None, role = None):
    chmo = User.objects.get(id = id)
    if name:
        chmo.name = name
    if email:
        chmo.email = email
    if role:
        chmo.role = role

def get_all_users():
    users = User.objects.filter(role = 'user').all()
    return users

#----------------------------------------------------------------------------------------------------

def create_category(name):
    Category(
        name = name
    ).save()

def get_category_by_name(name):
    return Category.objects.get(name = name)

def add_product(name, price, description, category_name):
    category = get_category_by_name(category_name)
    Product(
        name = name,
        price = price,
        description = description,
        category = category
    ).save()

def get_product_by_id(id):
    return Product.objects.get(id = id)

category = get_category_by_name('food')

#------------------------------------------gamemanager------------------------------------------
def add_genre(name):
    Genre(name = name).save()

def get_genre_by_name(name):
    try:
        genre = Genre.objects.get(name = name)
    except:
        genre = None
    if not genre:
        add_genre(name)
        genre = Genre.objects.get(name = name)
    return genre
    

def add_game(title, genres:tuple|list, release_date, rating:float):
    genres = [get_genre_by_name(genre_name) for genre_name in genres]
    game = Game(
        title = title,
        release_date = release_date,
        rating = rating
    )
    game.save()

    for genre in genres:
        game.genres.add(genre)



# add_game('dota 2', ['moba', 'rpg', 'strategy','competitive', 'action'], '2013-07-09', rating = 87)
# add_game('clash royale', ['strategy', 'competitive'], '2016-03-02', rating = 86)
# add_game('clash of clans', ['strategy', 'action'], '2012-08-02', rating = 90)

dota = Game.objects.filter(id = 1).first()
rpg = dota.genres.filter(name='strategy').first()
print(rpg.games.all())
print(dota.genres.all())