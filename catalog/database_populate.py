from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User, Category, Item

engine = create_engine('sqlite:///catlist.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

User1 = User(name="Anna Passos",
             email="anna@gmail.com",
             picture="https://yt3.ggpht.com/-1QP5KVYMxbo/AAAAAAAAAAI/"
             "AAAAAAAAAAA/djiAx3PhJ60/s900-c-k-no-mo-rj-c0xffffff/photo.jpg")
session.add(User1)
session.commit()

User2 = User(name="Maria Flora",
             email="maria@gmail.com",
             picture="https://athomaspointofview.files.wordpress.com/"
             "2015/08/3_525_1408990651.jpg")
session.add(User2)
session.commit()

User3 = User(name="Isa Linda",
             email="isa@gmail.com",
             picture="http://i1.wp.com/peopledotcom.files.wordpress.com/2016/"
             "10/madonna.jpg?crop=0px%2C129px%2C2000px%2C1334px&resize=2000%"
             "2C1333&ssl=1")
session.add(User3)
session.commit()

# Create all categories
category1 = Category(name="In the box")
session.add(category1)
session.commit()

category2 = Category(name="In the bag")
session.add(category2)
session.commit()

category3 = Category(name="Inside something")
session.add(category3)
session.commit()

category4 = Category(name="Just fighting")
session.add(category4)
session.commit()

category5 = Category(name="Just climbing")
session.add(category5)
session.commit()

category6 = Category(name="Just posing")
session.add(category6)
session.commit()

category7 = Category(name="Princess")
session.add(category7)
session.commit()

category8 = Category(name="Scared")
session.add(category8)
session.commit()

category9 = Category(name="Shy")
session.add(category9)
session.commit()

category10 = Category(name="Bored")
session.add(category10)
session.commit()

category11 = Category(name="Crazy")
session.add(category11)
session.commit()

category12 = Category(name="Charming")
session.add(category12)
session.commit()

# Create sample items
item1 = Item(name="Louis",
             description="Mussum Ipsum, cacilds vidis litro abertis. Pra la,"
             "depois divoltis porris, paradis. Quem manda na minha terra sou"
             "Euzis!  Admodum accumsan disputationi eu sit. Vide electram"
             "sadipscing et per.",
             picture_url="http://www.redbarninc.com/blog/wp-content/uploads/"
             "2015/02/it__s_a_cat_in_a_box_by_equinejumper2-d5375js.jpg",
             user_id=1, category_id=1)
session.add(item1)
session.commit()

item2 = Item(name="Batata",
             description="Suco de cevadiss, e um leite divinis, qui tem"
             "lupuliz, matis, aguis e fermentis. Copo furadis e disculpa de"
             "bebadis, arcu quam euismod magna. Delegadis gente finis,"
             "bibendum egestas augue arcu ut est. Interagi no me, cursus"
             "quis, vehicula ac nisi.",
             picture_url="http://pages.swcp.com/~jamiiweb/OtherCats/"
             "cat-inside.jpg",
             user_id=3, category_id=3)
session.add(item2)
session.commit()

item3 = Item(name="Amora",
             description="Mussum Ipsum, cacilds vidis litro abertis."
             " Nec orci ornare consequat. Praesent lacinia ultrices "
             "consectetur. Sed non ipsum felis. Paisis, filhis, espiritis"
             " santis. Quem manda na minha terra sou Euzis! Posuere libero"
             " varius. Nullam a nisl ut ante blandit hendrerit. Aenean sit",
             picture_url="https://img1.wsimg.com/fos/sales/cwh/8/images/cats"
             "-with-hats-shop-06.jpg",
             user_id=2, category_id=6)
session.add(item3)
session.commit()

item8 = Item(name="Ualeus",
             description="Mussum Ipsum, cacilds vidis litro abertis."
             " Nec orci ornare consequat. Praesent lacinia ultrices "
             "consectetur. Sed non ipsum felis. Paisis, filhis, espiritis"
             " santis. Quem manda na minha terra sou Euzis! Posuere libero"
             " varius. Nullam a nisl ut ante blandit hendrerit. Aenean sit",
             picture_url="https://i.ytimg.com/vi/cNycdfFEgBc/"
             "maxresdefault.jpg",
             user_id=1, category_id=8)
session.add(item8)
session.commit()

print "The Cats are UP!"
