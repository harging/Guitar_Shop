import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.brand import Brand
from models.item import Item
import repositories.item_repository as item_repo
import repositories.brand_repository as brand_repo

brands_blueprint = Blueprint("brands", __name__)

@brands_blueprint.route("/brands")
def brands():
    brands = item_repo.select_all()
    return render_template("brands/index.html", all_items = brands)

# NEW
# GET '/brands/new'
@brands_blueprint.route("/brands/new", methods=['GET'])
def new_brands():
    brands = brand_repo.select_all()
    return render_template("brands/new.html", all_brands = brands)

# CREATE
# POST '/items'
@brands_blueprintt.route("/items",  methods=['POST'])
def create_item():
    print(request.form)
    name = request.form['name']
    brand  = brand_repo.select(request.form['brand_id'])
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    item = Item(name, brand, description, stock_quantity, buying_cost, selling_price)
    item_repo.save(item)
    return redirect('/items')


# SHOW
# GET '/items/<id>'
@brands_blueprint.route("/items/<id>", methods=['GET'])
def show_item(id):
    item = item_repo.select(id)
    return render_template('items/show.html', item = item)

# EDIT
# GET '/items/<id>/edit'
@brands_blueprint.route("/items/<id>/edit", methods=['GET'])
def edit_item(id):
    item = item_repo.select(id)
    brands = brand_repo.select_all()
    return render_template('items/edit.html', item = item, all_brands = brands)

# UPDATE
# PUT '/items/<id>'
@brands_blueprint.route("/items/<id>", methods=['POST'])
def update_item(id):
    name = request.form['name']
    brand  = brand_repo.select(request.form['brand_id'])
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    item = Item(name, brand, description, stock_quantity, buying_cost, selling_price)
    item_repo.update(item)
    return redirect('/items')

# DELETE
# DELETE '/items/<id>'
@brands_blueprint.route("/items/<id>/delete", methods=['POST'])
def delete_item(id):
    item_repo.delete(id)
    return redirect('/items')