# T2A2 - API Webserver Project
## By Alicia Han
---

This application was created for assignment T2A2. The purpose of this application is for users to plan and organise a wedding.

[Github Repository Link](https://github.com/ahan-nz/API-Project-Wedding-Planner)

---

## Contents

* [Installation and Setup](#installation-and-setup)
* [R1: Problem Indentification](#r1-identify-the-problem-you-are-trying-to-solve-with-this-app)
* [R2: Problem Justification](#r2-why-is-it-a-problem-that-needs-solving)
* [R3: Database System](#r3-why-have-you-chosen-this-database-system-what-are-the-drawbacks-compared-to-others)
* [R4: ORM Functionalities and Benefits](#r4-identify-and-discuss-the-key-functionalities-and-benefits-of-an-orm)
* [R5: Endpoints](#r5-endpoints)
* [R6: ERD](#r6-erd)
* [R7: Third Party Services](#r7-detail-any-third-party-services-that-your-app-will-use)
* [R8: Models and Relationships](#r8-describe-your-projects-models-in-terms-of-the-relationships-they-have-with-each-other)
* [R9: Database Relations](#r9-discuss-the-database-relations-to-be-implemented-in-your-application)
* [R10: Planning and Tracking Tasks](#r10-describe-the-way-tasks-are-allocated-and-tracked-in-your-project)
* [References](#references)

---

### Installation and Setup

Inside the folder of the API application, type the following commands in terminal:

```
psql
```
Then to create the database:
```
CREATE DATABASE wedding_planner;
```
Next, connect to the new database:
```
\c wedding_planner;
```
Create a user with a password, then grant all privileges, for example:
```
CREATE USER planner_dev WITH PASSWORD 'wedding123';

GRANT ALL PRIVILEGES ON DATABASE wedding_planner TO planner_dev;
```
Open a new terminal window, inside the same folder as the source code, run the following to create and activate a virtual environment:
```
python3 -m venv .venv

source .venv/bin/activate
```
Install packages required:
```
python3 -m pip install -r requirements.txt
```
Change file '.env.sample' to just '.env', and update the contents, for example:
```
# Database connection string
DB_URI="postgresql+psycopg2://planner_dev:wedding123@localhost:5432/wedding_planner"

# JWT secret key
JWT_KEY="This is the secret key"
```
Finally, run the following cli commands to set up and run the Flask app:
```
flask db create

flask db seed

flask run
```
The port has been set to 8000, now we should be able to connect to http://127.0.0.1:8000/ via Postman or on our browser.

---

### R1 Identify the problem you are trying to solve with this app

The purpose of this app is to simplify and organise the task of wedding planning. The aim is make this often stressful task a better experience by giving brides and grooms a starting point on brainstorming and planning for their big day, and having the details all in one place. For the purposes of this assignment the scope has been limited, however there is potential to scale and add more features such as catering or florists.

---

### R2 Why is it a problem that needs solving?

Wedding planning can be a huge and daunting task with many variables, and most brides and grooms have little experience with event planning. There are a multitude of choices such as venues, catering and vendors, which can be difficult to track. In addition, wedding planners can be very costly, which can be unattainable for many couples who may be stretching their budget for the wedding. 

---

### R3 Why have you chosen this database system. What are the drawbacks compared to others?

PostgreSQL is a widely-adopted object-relational DBMS that I chose due to it's many advantages. Firstly it is open source and free to use, which keeps the initial cost low (if any). As a beginner in the field, it has a lower learning curve compared to some other database systems. In addition, as mentioned above, it is widely used in the industry and is supported by a large community with extensive forum discussions and documentation, hence there is help readily available if there are any issues. 

Despite being free to use, PostgreSQL is very feature-rich. It is highly extensible, which means new functions, data types, etc, can be added. There is a wide range of libraries and tools available for developers and is supported across all the common platforms including MacOS, Linux, and Windows (PostgreSQL, 2020). It is very scalable, and used with relational databases that can store large datasets in tables, utilising transactional Data Definition Language to easily implement mdifications to the database with minimal disruption to the framework. Although my application won't have a big database for this assignment, there is the potential to grow. It is also helpful to have the data in a rigid schema for ease of access and also to establish clear relationships between each entity.

PostgreSQL is ACID compliant, which stands for atomicity, consistency, isolation and durability. Atomacity refers to how every operation has to succeed for the transaction to succeed, avoiding unintential results from partial transactions. Consistency is sticking to the database constraints and isolation means transactions, even if happening at the same time, won't interfere with one another. Finally, durability refers to an up to date database once a transaction happens (MongoDB, 2023). This ensures a reliable database for my app that supports multiple users and high transactional loads if needed.

Last but not least, PostgreSQL is secure, so our users' details are better protected, user accounts can be authenticated and also set up with varying permission at handling the data.

Some of the drawbacks include some open source apps support MySQL but not PostgreSQL, and PostgreSQL also has slower performance metrics than MySQL (Dhruv, 2019) as it starts from the first row of a table in a relationship database and reads it sequentially. However these aren't as important as PostgreSQL being better at executing complex queries for this application, and that it's free to use. MySQL is also only ACID compliant in certain conditions. 

One could argue that PostgreSQL is also less flexible, compared to say MongoDB, in the sense that a table in a relational database cannot have extra fields outside of the set schema. However this is unlikely to be an issue with the limited entities that we have in this application.

---

### R4 Identify and discuss the key functionalities and benefits of an ORM

ORMs, or object relational mappers, allows the mapping of objects from an OOP language to a relational database. In this case, we're working with Python objects using SQLAlchemy.

A main functionality is to be able to work with classes and objects instead of having to write low level SQL queries to manipulate a relational database. Developers can take an object-orientated approach, with database entities as the objects. The benefit is that the code is more clean, organised, reusable and readable, and programmers can work in a language that they may be more proficient in (Tuama, 2022).

Another functionality is the support of multiple databases. It acts as the middleman between the database and the application, keeping the code database-agnostic. The benefit is that developers can switch to a different database system easily, e.g. PostgreSQL and MySQL, without needing to rewrite the entire code, as an ORM would handle the translation.

ORMs also enable the management of the database from our code, such as controlling the structure, with schemas defined in models. The ORM generates the tables, columns and relationships automatically, which is beneficial in eliminating manual schema creation and modification. In this application, each model class represents an entity in the relational database, such as users or venues. Each attribute, or column, is a field in the class, such as the email address or the first name of a user. The ORM tracks and synchronises any updates to objects with the database.

In addition, ORMs provide data validation mechanisms. Data integrity can be enforced by validations against data types and constraints, properly formatted and valid data means less inconsistencies and errors in the database. 

The above point also means that ORMs provide better security. Common vulnerabilities such as the risk of SQL injections are reduced with the input sanitisation. Moreover, security is also improved with being able to assign different levels of access to various users if necessary, maintaining data confidentiality (Abba, 2022).

As an ORM generates SQL queries behind the scenes, a potential drawback is that what is happening in the background can be abstract and less obvious to the developer during any troubleshooting. Furthermore, writing queries in SQL can offer more control, flexibility and customisation for fine tuning, compared to only using the ORM (LinkedIn, 2023).

---

### R5 Endpoints

---

### R6 ERD

![ERD](./docs/ERD.png)

This database consists of six normalised tables:

* Entity: Users

The first column is the primary key which uniquely identifies each user in the database, an id number that gets generated. It is followed by the first and last name of the user, a unique email address, a password and whether or not the user is admin, a Boolean value. All of these attributes are compulsory.

* Entity: Guests

This entity again starts with the unique identifier of id. Then there must be a first and last name. Email and phone numbers are optional, for example some weddings guests may be young children or other dependents who do not have their own contact information. There is a Boolean value indicating whether or not they have RSVP'ed and a foreign key of user id.

* Entity: Weddings

This entity has a unique generated id number as the primary key. Due to the scope of this project, I've kept it limited to who the wedding belongs to (the user) and where the wedding will be (the venue). These are represented as foreign keys. Future improvements can include other entities such as photographers or florists, etc.

* Entity: Venues

The primary key is a unique, generated id number. This column is followed by the street number, street name, phone, email and a foreign key of the city that the venue is in, all of which are compulsory. Then there are optional attributes for description, cost per head, minimum and maximum guests.

* Entity: Cities

This simply consists of the unique id number, the name of the city and the postcode. There is a foreign key for state id. There aren't CRUD routes for cities as the name and postcode of a city is unlikely to change, once set. I've added some examples of cities to be seeded into the database on command "flask db seed".

* Entity: States

As I'm basing my application in Australia, I added states for Australian addresses as part of a normalised data base. Again there is a unique id number as the primary key. As with cities, no CRUD routes are provided as once states are seeded into the database, modifications are unlikely to be needed. I've added some examples of states to be seeded into the database on command "flask db seed".

---

### R7 Detail any third party services that your app will use

---

### R8 	Describe your projects models in terms of the relationships they have with each other

---

### R9 Discuss the database relations to be implemented in your application

This database consists of five relations between six normalised tables, details about the entities were described in R6. I've added colours to the relations to explain each:
![ERD](./docs/ERDcoloured.png)

* Relationship in green: Users to Guests, One to Many

As seen in the ERD with the relationship linked in green, using Crow's Foot notation, every guest must be connected to a user, and a user can have none or many guests. This is because a user may not have added any guests to their wedding planning, but every guest entry made must be invited to someone's wedding. I've made guests associated with the user rather than the weddings entity as users may also decide to add guests first before making a wedding entry, therefore guests can exist without there being a weddings entity. In addition, guests can only be connected to one user as a guest's personal information is confidential and shouldn't be shared between multiple users. The foreign key is stored in the many table, which is 'guests', referring to the primary keys of 'users'.

* Relationship in blue: Users to Weddings, One to One

As highlighted in blue in the ERD, every wedding entry must be connected to a user. In addition, a user can only have one wedding entry maximum at a time, as brides and grooms are unlikely to be planning for more than one wedding at a time. Each user may or may not have created a wedding entry yet, hence the Crow's Foot symbol is 0 or 1 on the 'weddings' end. A wedding cannot exist without a user whereas a user won't necessarily have a wedding entry. The foreign key is stored in the optional table, which is 'weddings', referring to the primary keys of 'users'.

* Relationship in red: Venues to Weddings, One to Many

This relationship is shown in red in the ERD above. Every venue can be added to multiple different wedding entries, hence the one to many. A venue can also exist in the database without being linked to any wedding entries at all. For the purposes of this app, a wedding is assumed to be hosted at only one venue. The foreign key is stored in the many table, which is 'weddings', referring to the primary keys of 'venues'.

* Relationship in yellow: Cities to Venues, One to Many

This relation shown in yellow in the ERD links each venue to a city that it's located in. A city can have none or many venues, whereas it is only possible for a venue to be located in one city. I separated cities into a different table from the address attributes in venues to keep it DRY, as the same city is likely to be repeated between different venues. The foreign key is stored in the many table, which is 'venues', referring to the primary keys of 'cities'.

* Relationship in pink: States to Cities, One to Many

The relation in pink links each city to a state. A state can contain many cities whereas a city can only be in one state. I separated states into its own table to keep it DRY, as the same state is likely to be repeated between different cities. The foreign key is stored in the many table, which is 'cities', referring to the primary keys of 'states'.

---

### R10 Describe the way tasks are allocated and tracked in your project

I initially brainstormed ideas for a project on paper, and chose the most practical one to propose on Discord for educator approval.

I also formed a rough idea of the entities and relationships during this, which acted as the basis for my ERD.

* User Stories

This is where I started to think about the end goals of the application, from the point of view of the end user to improve customer satisfaction. I created several user stories from the point of view of the user, which is the bride/groom in this case. These will help with the planning stage of the application and ensure I start with the end in mind. My user stories were as follows:

1. As a user, I want to be able to create a user profile with ease and have my information secure. I also would like to be able to update or delete my profile.

2. As a user, I want to be able to create, read, update or delete a wedding event. I don't want other general users to be able to see or modify this information.

3. As an admin of the app, I want to have be able to view all data in entities and be able to perform CRUD on all models.

4. As a user, I want to be able to create/add/modify/delete guests and their information, such as contact details and whether or not they have RSVP'ed. I want this informatino to be accessible only to myself (and the admin).

5. As a user, I want to be able to create, read, update or delete potential venues and its information, like address, contact details, and costs. I may also want to be able to add my own notes in a description column.

I utilised Trello to help me track tasks throughout this project, with lists based on a Kanban board template, including:

* Backlog

This is a list of tasks that I have yet to start on. It helps me to plan and clarify the exact tasks that I need to complete. This will also include tasks that may be out of scope for this assignment that I can work on in future, including adding other vendors such as florists or wedding dress fittings.

* In Progress

These are the tasks that I am currently working on, it's useful not only for tracking my progress but also to make sure I don't have too many cards in this list at the same time. It would also be useful if I were working in a team so we are update to date with each others' progress.

* Review

These are the tasks that I have completed but yet to finalise. For example my ERD card went here once I finished the initial plan, but it was still  subject to change as I built my app. This section would also include code that I've written but yet to be tested fully on Postman.

* Done

These are tasks that I have completed and no longer need to revisit.

The Trello board allowed me to grasp the big picture of my progress throughout this assignment and split my tasks into smaller jobs. THis is a screenshot of my board halfway through my project, as an example:

---

### References

* PostgreSQL Documentation. (2020). 1. What Is PostgreSQL? [online] Available at: https://www.postgresql.org/docs/current/intro-whatis.html.

* MongoDB. (2023). What Does ACID Compliance Mean? | An Introduction. [online] Available at: https://www.mongodb.com/databases/acid-compliance#:~:text=Well%2C%20ACID%20stands%20for%20atomicity.

* Dhruv, S. (2019). Pros and Cons of using PostgreSQL for Application Development. [online] Aalpha. Available at: https://www.aalpha.net/blog/pros-and-cons-of-using-postgresql-for-application-development/.

* LinkedIn. (2023). What are the benefits and drawbacks of using ORM for complex queries and aggregations? [online] Available at: https://www.linkedin.com/advice/0/what-benefits-drawbacks-using-orm-complex-queries#:~:text=One%20of%20the%20main%20benefits/.

* Tuama, D.Ó. (2022). Object Relational Mapping: What is an ORM? [online] Code Institute Global. Available at: https://codeinstitute.net/global/blog/object-relational-mapping/.

* Abba, I.V. (2022). What is an ORM – The Meaning of Object Relational Mapping Database Tools. [online] freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/.

