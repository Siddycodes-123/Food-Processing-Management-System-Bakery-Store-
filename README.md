# Food-Processing-Management-System-Bakery-Store-

# 🍞 Food Processing Management System (Bakery Store)

This project was created as our **Class 12 Computer Science Final Project**.  
It is a **Food Processing Management System** built around a **Bakery Store**, integrating **Python** with **MySQL** to manage inventory, counter items, and vendor orders.

---

## 📌 Project Overview
The system helps bakery staff efficiently track and manage:
- 🥖 **Ration stock** (raw materials like flour, sugar, etc.)
- 🍩 **Products** (food items available on the counter)
- 🥛 **Crockery items** (utensils and tools required in the store)
- 🛒 **Retailers/Vendors** (for ordering when stock is unavailable)

This project demonstrates how **Python can interact with MySQL** to build a practical store management system.

---

## ⚙️ Features
- **Ration Management** → Add, update, and check raw material availability  
- **Product Management** → Track food items available for sale  
- **Crockery Management** → Manage stock of bakery utensils/crockery  
- **Retailer Management** → Store vendor names & contact details for quick restocking  
- **Editable Stock** → Update item quantities and availability in real time  
- **Persistent Database** → Data stored in MySQL for reliability  
- **User-Friendly CLI** → Simple command-line interface  

---

## 🛠️ Tech Stack
- **Python 3.x** (application logic)  
- **MySQL** (database)  
- **mysql-connector-python** (Python-MySQL connector)  

---

## 🗄️ Database Schema (MySQL)

The project uses four main tables:  

### 1. Ration
+----------------+---------------+
| Ration         | Quantity_In_Kg|
+----------------+---------------+
| Flour          | 35            |
| Sugar          | 35            |
| Salt           | 3             |
| Baking Soda    | 4             |
| Baking Powder  | 3             |
| Cocoa Powder   | 5             |
| Vanilla extract| 8             |
| Cow Milk       | 17            |
| Cherries       | 4             |
| Cream          | 8             |
| Butter         | 11            |
| Vegetable Oil  | 15            |
+----------------+---------------+

### 2. Product
+----------+-----------+------+-----------+
| SerialNo | Products  | Cost | TotalUnits|
+----------+-----------+------+-----------+
|    1     | Cake      | 750  |    26     |
|    2     | Milk      | 50   |   100     |
|    3     | Chocolate | 60   |    79     |
|    4     | Bread     | 30   |    56     |
|    5     | Puff      | 20   |    47     |
|    6     | Creamroll | 30   |    36     |
+----------+-----------+------+-----------+

### 3. Crockery
+-----+----------+----------------+
| sno | itemcode | itemname       |
+-----+----------+----------------+
|  1  |   289    | Plate          |
|  2  |   659    | Knife          |
|  3  |   721    | Blender        |
|  4  |   524    | Chopping board |
|  5  |   241    | Cake Slicer    |
|  6  |   213    | Dish Rack      |
|  7  |   872    | Colander       |
|  8  |   231    | Fork           |
|  9  |   752    | Wok            |
| 10  |   852    | Rolling Pin    |
+-----+----------+----------------+

### 4. Retailer
+----+------------+--------------+------------+
| No | retailerID | retailer     | phoneno    |
+----+------------+--------------+------------+
|  1 |   1342582  | Anil Kumar   | 9812494121 |
|  2 |   1812494  | Suresh Bhatt | 8128847261 |
|  3 |   2778534  | Nilesh Rana  | 9329583951 |
+----+------------+--------------+------------+


⚠️ The original `.sql` setup file is not included.  
You can create tables in MySQL using the schema description above.

---


