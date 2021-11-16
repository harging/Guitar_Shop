from db.run_sql import run_sql
import pdb

from models.item import Item
from models.brand import Brand
import repositories.brand_repository as brand_repo


def save(item):
    sql = "INSERT INTO items (name, brand_id, description, stock_quantity, buying_cost, selling_price) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [item.name, item.brand.id, item.description, item.stock_quantity, item.buying_cost, item.selling_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    item.id = id
    return item

def select_all():
    items = []

    sql = "SELECT * FROM items"
    results = run_sql(sql)

    for row in results:
        brand = brand_repo.select(row['brand_id'])
        item = Item(row['name'], brand, row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['id'])
        items.append(item)
    return items

def select(id):
    item = None
    sql = "SELECT * FROM items WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        brand = brand_repo.select(result['brand_id'])
        item = Item(result['name'], brand, result['description'], result['stock_quantity'], result['buying_cost'], result['selling_price'], result['id'])
    return item

def delete_all():
    sql = "DELETE  FROM items"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM items WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(item):
    sql = "UPDATE items SET (name, description, stock_quantity, buying_cost, selling_price, brand_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [item.name, item.description, item.stock_quantity, item.buying_cost, item.selling_price, item.brand.id, item.id]
    run_sql(sql, values)
