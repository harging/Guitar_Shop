from db.run_sql import run_sql

from models.item import Item
from models.brand import Brand

def save(brand):
    sql = "INSERT INTO brands (name, active) VALUES (%s, %s) RETURNING *"
    values = [brand.name, brand.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    brand.id = id
    return brand


def select_all():
    brands = []

    sql = "SELECT * FROM brands"
    results = run_sql(sql)

    for row in results:
        brand = Brand(row['name'], row['active'], row['id'])
        brands.append(brand)
    return brands


def select(id):
    brand = None
    sql = "SELECT * FROM brands WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        brand = Brand(result['name'], result['active'], result['id'])
    return brand


def delete_all():
    sql = "DELETE  FROM brands"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM brands WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(brand):
    sql = "UPDATE brands SET (name, status) = (%s, %s, %s) WHERE id = %s"
    values = [brand.id, brand.name, brand.active]
    run_sql(sql, values)

def items(brand):
    items = []

    sql = "SELECT * FROM items WHERE brand_id = %s"
    values = [brand.id]
    results = run_sql(sql, values)

    for row in results:
        item = Item(row['id'], row['name'], row['brand_id'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'])
        items.append(item)
    return items
