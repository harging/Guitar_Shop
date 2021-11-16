from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.item import Item
import repositories.item_repository as item_repo
import repositories.brand_repository as brand_repo

items_blueprint = Blueprint("items", __name__)

@items_blueprint.route("/items")
def items():
    items = item_repo.select_all()
    return render_template("items/index.html", all_items = items)

# NEW
# GET '/items/new'
@items_blueprint.route("/items/new", methods=['GET'])
def new_items():
    brands = brand_repo.select_all()
    return render_template("items/new.html", all_brands = brands)

# CREATE
# POST '/items'
@items_blueprint.route("/items",  methods=['POST'])
def create_item():
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
@items_blueprint.route("/items/<id>", methods=['GET'])
def show_item(id):
    item = item_repo.select(id)
    return render_template('items/show.html', item = item)

# EDIT
# GET '/items/<id>/edit'
@items_blueprint.route("/items/<id>/edit", methods=['GET'])
def edit_item(id):
    item = item_repo.select(id)
    brands = brand_repo.select_all()
    return render_template('items/edit.html', item = item, all_brands = brands)

# UPDATE
# PUT '/items/<id>'
@items_blueprint.route("/items/<id>", methods=['POST'])
def update_item(id):
    name = request.form['name']
    brand  = brand_repo.select(request.form['brand_id'])
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    item = Item(name, brand, description, stock_quantity, buying_cost, selling_price, id)
    item_repo.update(item)
    return redirect('/items')

# DELETE
# DELETE '/items/<id>'
@items_blueprint.route("/items/<id>/delete", methods=['POST'])
def delete_item(id):
    item_repo.delete(id)
    return redirect('/items')