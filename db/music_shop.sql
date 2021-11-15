DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS brands;

CREATE TABLE brands (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  active Boolean
);

CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  stock_quantity INT,
  buying_cost INT,
  selling_price INT,
  brand_id INT REFERENCES brands(id)
);