---1. Insert dump (my_items) to your local database.
---	Create additional table phones with fields:
---		id, phone_name, company_id, user_id
CREATE TABLE phones (
	id int NOT NULL AUTO_INCREMENT,
	phone_name varchar(255) NULL,
	company_id int NOT NULL,
	user_id int NOT NULL,
	PRIMARY KEY (id)
);

---	Create additional table phone_companies with fields:
---		id, name
CREATE TABLE phone_companies (
	id int NOT NULL AUTO_INCREMENT,
	name varchar(255) NULL,
	PRIMARY KEY (id)
);

---Write select and save it to file to get users is developers.
/*
mysql -u root -p my_items -e "SELECT * FROM users WHERE is_developer=1;" > developers.txt
*/

---	Insert xiaomi, apple, samsung to companies.
INSERT INTO phone_companies (name)
VALUES ('xiaomi'), ('apple'), ('samsung');

---	Insert 3 phone (with any data) to phones.
INSERT INTO phones (phone_name, company_id, user_id)
VALUES ('Xiaomi Redmi Note 9', 1, 4),
       ('Apple iPhone 12 Pro Max', 2, 1), 
       ('Samsung Galaxy A51', 3, 3);

---	Write select and save it to file to get phones where company_id=XIAOMI COMPANY ID.
/*
mysql -u root -p my_items -e "SELECT * FROM phones WHERE company_id IN (SELECT id FROM phone_companies WHERE name = 'xiaomi');" > xiaomi_phones.txt
*/

---2.* Select all users which have phones.
SELECT * FROM users
WHERE id IN (SELECT user_id FROM phones);

