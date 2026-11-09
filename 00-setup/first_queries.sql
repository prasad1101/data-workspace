CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    product TEXT,
    price NUMERIC,
    qty INT);

INSERT INTO orders(product, price, qty) VALUES
('Laptop',55000,2),
('Mouse', 500, 10),
('Monitor', 12000, 3);

SELECT product, price * qty AS total FROM orders;

SELECT * FROM orders;