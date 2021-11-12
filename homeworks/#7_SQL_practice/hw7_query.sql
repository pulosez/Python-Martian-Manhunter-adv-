--Modify table products add user_id as foreign key
ALTER TABLE products ADD COLUMN user_id int NOT NULL;
UPDATE products SET user_id = 1 WHERE id = 1;
ALTER TABLE products ADD FOREIGN KEY (user_id) REFERENCES users(id);

--Select users their products, collections and images and write this query to file.
SELECT users.id, users.first_name, users.last_name,
products.title, products.price, categories.title, product_images.file
FROM users
JOIN products ON users.id = products.user_id
JOIN categories_products ON products.id = categories_products.product_id
JOIN categories  ON categories_products.category_id = categories.id
JOIN product_images ON products.id = product_images.product_id

