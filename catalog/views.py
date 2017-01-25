import os
import random
import string

from flask import Flask
from flask import (flash, render_template, url_for, jsonify,
                   request, redirect, send_from_directory)

from werkzeug import secure_filename

from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

from models import Base, User, Category, Item

# secret key to encrypt session cookie
SECRET_KEY = ''.join(random.choice(string.ascii_uppercase +
                     string.digits) for x in xrange(32))

# define default values for file management
UPLOAD_FOLDER = '/vagrant/catalog/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = SECRET_KEY

# connect to database and create db session
engine = create_engine('sqlite:///catlist.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# GENERAL FUNCTIONS AND ROUTES -->

def categoryMenu():
    '''Get categories from DB for menu navigation'''
    menuNav = session.query(Category).all()
    return menuNav


def allowed_file(filename):
    '''Check if a file extension is valid'''
    return ('.' in filename and filename.rsplit('.', 1)[1]
            in ALLOWED_EXTENSIONS)


def delete_image(filename):
    '''Delete a image from server'''
    try:
        os.remove(os.path.join(UPLOAD_FOLDER, filename))
    except OSError:
        print "Sorry, we couldn't delete the image %s" % filename


@app.route('/picture/<filename>')
def show_image(filename):
    '''Get images uploaded'''
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# THE JSON API ENDPOINTS -->

@app.route('/cats/JSON')
def catlistsJSON():
    '''Return all items with categories as JSON file'''
    categories = categoryMenu()
    return jsonify(categories=[r.serialize for r in categories])


@app.route('/catlover/<int:user_id>/JSON/')
def listJSON(user_id):
    '''Return a user list as JSON file'''
    user = session.query(User).filter_by(id=user_id).one()
    return jsonify(User=user.serialize)


@app.route('/cat/<int:item_id>/JSON/')
def itemJSON(item_id):
    '''Return a single item as JSON file'''
    item = session.query(Item).filter_by(id=item_id).one()
    return jsonify(Item=item.serialize)


# PRIMARY ROUTES -->

@app.route('/')
def mainPage():
    '''The Homepage'''
    menuNav = categoryMenu()

    items = session.query(Item).order_by(desc(Item.id))
    return render_template('index.html', menuNav=menuNav, items=items)


@app.route('/catlover/<int:user_id>/')
def showList(user_id):
    '''A User's list page '''
    menuNav = categoryMenu()

    user = session.query(User).filter_by(id=user_id).one()
    items = (session.query(Item).filter_by(user_id=user_id).order_by(
             desc(Item.category_id)).all())
    return render_template('list.html',
                           menuNav=menuNav,
                           user=user,
                           items=items)


@app.route('/catlover/<int:user_id>/delete/', methods=['GET', 'POST'])
def deleteList(user_id):
    menuNav = categoryMenu()

    user = session.query(User).filter_by(id=user_id).one()
    items = session.query(Item).filter_by(user_id=user_id).all()

    if request.method == 'POST':
        for item in items:
            session.delete(item)
            print "List deleted!"

        session.delete(user)
        print "User deleted!"
        session.commit()
        return redirect(url_for('mainPage'))
    else:
        return render_template('list_delete.html', menuNav=menuNav, user=user)


@app.route('/category/<int:category_id>/cats/')
def showCategory(category_id):
    '''Show items to a specific category.'''
    menuNav = categoryMenu()

    category = session.query(Category).filter_by(id=category_id).one()
    items = (session.query(Item).filter_by(category_id=category_id).order_by(
             desc(Item.id)).all())
    return render_template('category.html',
                           menuNav=menuNav,
                           category=category,
                           items=items)


@app.route('/cat/<int:item_id>/')
def showItem(item_id):
    '''Handler to Single Item page'''
    menuNav = categoryMenu()

    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('item.html', menuNav=menuNav, item=item)


@app.route('/catlover/<int:user_id>/newcat/', methods=['GET', 'POST'])
def addItem(user_id):
    '''Handler to add a new Item'''
    user = session.query(User).filter_by(id=user_id).one()
    user_id = user.id

    if request.method == 'POST':
        if not request.form['name']:
            flash("Your cat needs a name")
            return redirect(url_for('addItem', user_id=user_id))

        if not request.form['description']:
            flash("C'mon! One line about your cat!")
            return redirect(url_for('addItem', user_id=user_id))

        category = (session.query(Category).filter_by(
                    name=request.form['category']).one())
        newItem = Item(category=category,
                       name=request.form['name'],
                       description=request.form['description'],
                       user_id=user.id)

        picture_filename = request.files['picture_file']

        if picture_filename and allowed_file(picture_filename.filename):
            filename = secure_filename(picture_filename.filename)
            if os.path.isdir(app.config['UPLOAD_FOLDER']) is False:
                os.mkdir(app.config['UPLOAD_FOLDER'])
            picture_filename.save(os.path.join(
                                  app.config['UPLOAD_FOLDER'], filename))
            newItem.picture_filename = filename
        elif request.form['picture_url']:
            newItem.picture_url = request.form['picture_url']
        else:
            flash("Wow! Your cat deserves a picture! Upload it"
                  " or give us a link, please!")
            return redirect(url_for('addItem', user_id=user_id))

        session.add(newItem)
        session.commit()

        flash("Perrrrfect! Your amazing cat is up!")
        item_id = newItem.id
        return redirect(url_for('showItem', item_id=item_id))

    else:
        categories = categoryMenu()
        return render_template('item_new.html',
                               categories=categories,
                               user=user)


@app.route('/cat/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem(item_id):
    '''To edit an item.'''
    item = session.query(Item).filter_by(id=item_id).one()

    if request.method == 'POST':
        if not request.form['name']:
            flash("Your cat needs a name")
            return redirect(url_for('editItem', item_id=item_id))
        else:
            if request.form['name'] != item.name:
                item.name = request.form['name']

        if not request.form['description']:
            flash("C'mon! One line about your cat!")
            return redirect(url_for('editItem', item_id=item_id))
        else:
            if request.form['description'] != item.description:
                item.description = request.form['description']

        editedCategory = (session.query(Category).filter_by(
                    name=request.form['category']).one())
        if editedCategory != item.category:
            item.category = editedCategory

        picture_filename = request.files['picture_file']

        if picture_filename and allowed_file(picture_filename.filename):
            if item.picture_filename:
                delete_image(item.picture_filename)
            filename = secure_filename(picture_filename.filename)
            if os.path.isdir(app.config['UPLOAD_FOLDER']) is False:
                os.mkdir(app.config['UPLOAD_FOLDER'])
            picture_filename.save(os.path.join(
                                  app.config['UPLOAD_FOLDER'], filename))
            item.picture_filename = filename
            item.picture_url = None
        elif not picture_filename and request.form['picture_url']:
            item.picture_url = request.form['picture_url']
            if item.picture_filename:
                delete_image(item.picture_filename)
                item.picture_filename = None

        session.add(item)
        session.commit()

        flash("Your cat has changed!")
        item_id = item.id
        return redirect(url_for('showItem', item_id=item_id))

    else:
        categories = categoryMenu()
        return render_template('item_edit.html',
                               categories=categories,
                               item=item)


@app.route('/cat/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem(item_id):
    '''To delete an item.'''
    item = session.query(Item).filter_by(id=item_id).one()

    if request.method == 'POST':
        if item.picture_filename:
            delete_image(item.picture_filename)
        session.delete(item)
        session.commit()

        user = session.query(User).filter_by(id=item.user_id).one()
        user_id = user.id
        flash("Your cat's gone! :-(")
        return redirect(url_for('showList', user_id=user_id))
    else:
        menuNav = categoryMenu()
        return render_template('item_delete.html',
                               menuNav=menuNav,
                               item=item)


@app.errorhandler(404)
def notFound(exc):
    menuNav = categoryMenu()
    return render_template('404.html', menuNav=menuNav), 404

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
