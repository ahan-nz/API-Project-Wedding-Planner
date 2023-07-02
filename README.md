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
    * [Auth Routes](#auth-routes)
    * [Users Routes](#users-routes)
    * [Guests Routes](#guests-routes)
    * [Venues Routes](#venues-routes)
    * [Weddings Routes](#weddings-routes)
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

### Auth Routes

#### 1. /register

* Methods: POST

* Description: Creating a new user profile in the database

* Request Parameters: None

* Authentication: None

* Authorisation: None

* Request Body: 

```
{
    "f_name":"John",
    "l_name":"Kim",
    "email":"john@mail.com",
    "password":"Thisisjohn123%"
}
```

* Request Response:

HTTP Status Code: 201 CREATED

```
{
    "id": 4,
    "f_name": "John",
    "l_name": "Kim",
    "email": "john@mail.com",
    "is_admin": false
}
```

* Error Handling:

Scenario: Email address is already registered

Error code: 409 CONFLICT

Error Message: 
```
{
    "error": "Email address already in use"
}
```

Scenario: Missing field for f_name (same applies to l_name, email and password)

Error code: 400 BAD REQUEST

Error Message:
```
{
    "error": "The field 'f_name' is required."
}
```

Scenario: Password is invalid

Error code: 400 BAD REQUEST

Error Message:
```
{
    "error": {
        "password": [
            "Password must contain a minimum of eight characters, at least one uppercase letter, one lowercase letter, one number and one special character."
        ]
    }
}
```
There are also customised error messages for invalid email addresses and invalid symbols first and last names.

#### 2. /login

* Methods: POST

* Description: User login and receiving JWT token

* Request Parameters: None

* Authentication: None

* Authorisation: None

* Request Body: 

```
{
    "email":"hello@sallysmith.com",
    "password":"ThisisSally1!"
}
```

* Request Response: 

HTTP Status Code: 200 OK

```
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4ODI3MzA5MiwianRpIjoiZjgxMGI5MWYtNGM3Ni00NzdkLTlmNWEtYjQ2ZTJhM2NhYWM2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MiwibmJmIjoxNjg4MjczMDkyLCJleHAiOjE2ODgzMTYyOTJ9.XAWM1RCb5Yub6kRXkUnW6ZQBqBr7vZ5WRoblCgHYYlQ",
    "user": {
        "id": 2,
        "f_name": "Sally",
        "l_name": "Smith",
        "email": "hello@sallysmith.com",
        "is_admin": false
    }
}
```

* Error Handling:

Scenario: Email or password is incorrect

Error code: 401 UNAUTHORIZED

Error message:
```
{
    "error": "Invalid email address or password"
}
```

Scenario: Email or password is missing

Error code: 400 BAD REQUEST

Error message:
```
{
    "error": "Email and password are required"
}
```

### Users Routes

#### 1. /users

* Methods:

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

#### 2. /users/\<int:user_id>

* Methods: PUT, PATCH

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

#### 3. /users/\<int:user_id>

* Methods: DELETE

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

### Guests Routes

#### 1. /guests

* Methods: GET

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

#### 2. /guests/\<int:user_id>

* Methods: GET

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

#### 3. /guests

* Methods: POST

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

#### 4. /guests/\<int:user_id>

* Methods: PUT, PATCH

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

#### 5. /guests/\<int:user_id>

* Methods: DELETE

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

### Venues Routes

#### 1. /venues

* Methods: GET

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

#### 2. /venues/\<int:user_id>

* Methods: GET

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

#### 3. /venues

* Methods: POST

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

#### 4. /venues/\<int:user_id>

* Methods: PUT, PATCH

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

#### 5. /venues/\<int:user_id>

* Methods: DELETE

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

### Weddings Routes

#### 1. /weddings

* Methods: GET

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

#### 2. /weddings/\<int:user_id>

* Methods: GET

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

#### 3. /weddings

* Methods: POST

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

#### 4. /weddings/\<int:user_id>

* Methods: PUT, PATCH

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

#### 5. /weddings/\<int:user_id>

* Methods: DELETE

* Description:

* Request Parameters:

* Authentication:

* Authorisation:

* Request Body:

* Request Response:

* Error Handling:

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

* SQLAlchemy

SQLAlchemy is an open source ORM and SQL toolkit. It is used in the app to act as a bridge between high level Python programming language and the relational database. Python objects are mapped to database tables and Python code is encapsulated and translated into SQL in the background to query and manipulate data. SQLAlchemy is database agnostic and supports popular database systems including PosrtgreSQL, which is what this app uses, in addition to MySQL, SQLite, etc (TutorialsPoint, n.d.). 

* Flask-Marshmallow

This is an extension that integrates Marshmallow with a Flask app. Marshmallow is a library used in this app to serialise and deserialise complex objects into Python datatypes, such as JSON. It is also used to validate incoming data, ensuring data consistency and integrity. Moreover, it supports relationships between objects such as foreign key references and nested fields (Mwaura, 2021).

* Marshmallow-SQLAlchemy

This is an extension for Marshmallow that integrates it with SQLAlchemy. It allows for seamless serialisation and deserialisation of SQLAlchemy models and automatically generates Marshmallow schemas.

* Psycopg2

Psycopg2 is a popular database adapter designed for PostgreSQL. It is required as SQLAlchemy is a database agnostic ORM so it cannot interact with the database directly. Psycopg2 helps with making our code more reliable as it automatically does the conversion between Python objects and PostgreSQL datatypes (Psycopg, 2021).

* Python-Dotenv

Python-Dotenv is a library that assists in configuring environment variables, developers can keep configuration settings and secret keys in a separate file from the application code for better security. In this app, we have a .env file that stores the database connection stream and secret key. There is also a .flaskenv file with details such as the port (8000 in this case), debug mode and also where to run the app from (PyPI, 2023).

* Flask-Bcrypt

Bcrypt is a password hashing library for Python, Flask-Bcrypt is an extension of Flask that streamlines the process of encryption and verification of passwords. In this app, user passwords are hashed before being stored in the database. During verication, it checks whether the hashed user input matches the hashed password that is stored. A random salt value is included during the hashing process to add another layer of security. It is also designed to be computationally expensive and slow to make it resistant to brute-force attacks. This improves the security of our application and user data (GeeksforGeeks, 2023).

* Flask-JWT-Extended

This is a Flask extension that provides support for JWT authentication. It creates JSON web tokens with `create_access_token()`, and `jwt_required()` is used to protect routes from unauthorised access. The generated token, stored in a session in this app, is sent back to server in a header with any client requests to show authorisation, this also means users don't have to login with every request. This app also uses `get_jwt_identity()` to retrieve the identity of the JWT (Flask-JWT-Extended, n.d.). 

---

### R8 	Describe your projects models in terms of the relationships they have with each other

All models in this project are stored in a 'models' folder inside the source code folder. Each model is a Python class, representing an entity in the relational database. Each column, or field, is an attribute of the entity. SQLAlchemy was used to create the model class structures, including the columns, data types and any constraints.

* The User Model

```
# SQLAlchemy creates table structure with columns and data types
class User(db.Model):
    # Renames table to plural based on convention
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50), nullable=False)
    l_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    wedding = db.relationship('Wedding', back_populates='user', cascade='all, delete') # When a user is deleted, the wedding will also be deleted
    guests = db.relationship('Guest', back_populates='user', cascade='all, delete') # When a user is deleted, associated guests will also be deleted


# JSON (de)serialization with Marshmallow
class UserSchema(ma.Schema):
    f_name = fields.String(validate=And(Length(min=1, error='First name needs at least one character.'), Regexp('^[a-zA-Z ]+$', error='Only letters and spaces are allowed.')))
    l_name = fields.String(validate=And(Length(min=1, error='Last name needs at least one character.'), Regexp('^[a-zA-Z ]+$', error='Only letters and spaces are allowed.')))
    password = fields.String(validate= Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[#+-=@$!%*?&])[A-Za-z\d@$#$^()!%*?&]{8,}$', error='Password must contain a minimum of eight characters, at least one uppercase letter, one lowercase letter, one number and one special character.'))
    email = fields.String(validate= Regexp('^[a-zA-Z0-9.!#$%&*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$', error="Please provide a valid email address"))
    is_admin = fields.Boolean()

    class Meta:
        fields = ('id', 'f_name', 'l_name', 'email', 'password', 'is_admin')
        ordered = True # Orders keys in the same order as above
```
The user model is related to the wedding model with a one to one relationship, and to the guest model with a one to many relationship. The unique id of the user model, the primary key, is used as a foreign key by the wedding and guest models. `db.relationship` is set up on both ends so the two models can be mapped together, the `back_populates` argument specifies which column to link with when the tables are joined. Cascade delete is set up so that if a user is deleted, its associated wedding and guests will also be deleted. Marshmallow is used to convert SQLAlchemy models into JSON. 

* The Guest Model

```
class Guest(db.Model):
    # Renames table to plural based on convention
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50), nullable=False)
    l_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String) # Phone and email optional, e.g. child who doesn't have their own contact information
    email = db.Column(db.String)
    is_rsvp = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='guests') # No cascade delete as user shouldn't be deleted when a guest is deleted


# JSON (de)serialization with Marshmallow
class GuestSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['f_name', 'l_name'])
    f_name = fields.String(validate=And(Length(min=1, error='First name needs at least one character.'), Regexp('^[a-zA-Z ]+$', error='Only letters and spaces are allowed.')))
    l_name = fields.String(validate=And(Length(min=1, error='Last name needs at least one character.'), Regexp('^[a-zA-Z ]+$', error='Only letters and spaces are allowed.')))
    phone= fields.String(validate= Regexp('^[0-9 ()+]+$', error="Please provide a valid phone number"))
    email = fields.String(validate= Regexp('^[a-zA-Z0-9.!#$%&*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$', error="Please provide a valid email address"))
    is_rsvp = fields.Boolean()

    class Meta:
        fields = ('id', 'f_name', 'l_name', 'phone', 'email', 'is_rsvp', 'user')
        ordered = True # Orders keys in the same order as above
```
Each guest is related to a user with a foreign key in the Guest model, of user_id, linking to each primary key, the id, in the User model. Again, `db.relationship` and `back_populates` have been set up to refer to the other side of the relationship. Note that in this case, there is no cascade delete, because if a Guest is deleted, the User should not be deleted.
A nested field has been set up for user inside the Guest schema. This is so Marshmallow knows which schema to use to process the user attribute. We can see the nested user when we return a guest in JSON format:
```
{
    "id": 4,
    "f_name": "Eddy",
    "l_name": "Chan",
    "phone": "0434387110",
    "email": "beans@shibainu.com",
    "is_rsvp": true,
    "user": {
        "f_name": "Chris",
        "l_name": "Lee"
    }
}
```

* The State Model

```
# SQLAlchemy creates table structure with columns and data types
class State(db.Model):
    # Renames table to plural based on convention
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    cities = db.relationship('City', back_populates='state', cascade='all, delete') # When a state is deleted, all cities in the state will be deleted


# JSON (de)serialization with Marshmallow
class StateSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
```
This application is based in Australia and Australian addresses have states. The state model is related to the city model in a one to many relationship, where each state contains multiple cities but each city can only belong to one state. Each state is assigned a unique id, the primary key, which is used as a foreign key in the city model. `db.relationship` has been setup and cascade delete was added so that if a state is deleted off the database, then its cities will also be deleted.

* The City Model

```
# SQLAlchemy creates table structure with columns and data types
class City(db.Model):
    # Renames table to plural based on convention
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    postcode = db.Column(db.Integer, nullable=False)

    state_id = db.Column(db.Integer, db.ForeignKey('states.id', ondelete='CASCADE'), nullable=False)
    state = db.relationship('State', back_populates='cities') # No cascade delete as the state shouldn't be deleted when a city is deleted
    venues = db.relationship('Venue', back_populates='city', cascade='all, delete') # When a city is deleted, all venues in the city will also be deleted

# JSON (de)serialization with Marshmallow
class CitySchema(ma.Schema):
    state = fields.Nested('StateSchema', exclude=['id'])

    class Meta:
        fields = ('id', 'name', 'postcode', 'state')
```
The city model is linked to states with a many to one relationship as described previously, linked by the foreign key of state_id. It is also related to the venue model, with a one to many relationship. This indicates that each city can have many venues, whereas each venue can only be in one city. A `db.relationship` has been set up for each of the relations so SQLAlchemy knows what each end of the relationship is. What is different is that cascade delete was only set for venues. This is because when a city is deleted, the venues in that city will also be deleted but the state that the city is in shouldn't be deleted. Furthermore, we can see that `fields.Nested` was specified for the state so that Marshmallow knows to refer to the State schema during JSON serialisation.

* The Venue Model
```
# SQLAlchemy creates table structure with columns and data types
class Venue(db.Model):
    # Renames table to plural based on convention
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    street_number = db.Column(db.Integer, nullable=False)
    street_name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.Text())
    cost_per_head = db.Column(db.Integer)
    min_guests = db.Column(db.Integer)
    max_guests = db.Column(db.Integer)

    city_id = db.Column(db.Integer, db.ForeignKey('cities.id', ondelete='CASCADE'), nullable=False)
    city = db.relationship('City', back_populates='venues') # No cascade delete as when a venue is deleted, the city shouldn't be deleted.
    weddings = db.relationship('Wedding', back_populates='venue') # No cascade delete as when a venue is deleted, the wedding entry shouldn't be deleted.


# JSON (de)serialization with Marshmallow
class VenueSchema(ma.Schema):
    city = fields.Nested('CitySchema', exclude=['id'])
    name = fields.String(validate=Length(min=1, error='Name of venue needs at least one character.'))
    street_number = fields.Integer()
    street_name = fields.String(validate=Length(min=2, error='Street name needs at least two characters.'))
    phone= fields.String(validate= Regexp('^[0-9 ()+]+$', error="Please provide a valid phone number"))
    email = fields.String(validate= Regexp('^[a-zA-Z0-9.!#$%&*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$', error="Please provide a valid email address"))
    cost_per_head = fields.Integer()
    min_guests = fields.Integer()
    max_guests = fields.Integer()
    city_id = fields.Integer()

    class Meta:
        fields = ('id', 'name', 'street_number', 'street_name', 'phone', 'email', 'description', 'cost_per_head', 'min_guests', 'max_guests', 'city_id', 'city')
        ordered = True # Orders keys in the same order as above
```
The venue model is related to the city model with a foreign key of city_id, as described previously. It is also related to the wedding model with a one to many relationship, where the primary key of the venue model is used as a foreign key in the wedding model. `db.relationship` has been set up for each of the two relationships here to specify each side of the relationship to SQLAlchemy; no cascade delete is set so that if a venue gets deleted, the wedding entry and the city will still exist. Inside the venue schema, city is also specified as a nested field so that Marshmallow knows to refer to the CityScheme during JSON serialisation. When a venue is returned in JSON format, we can see the nested City, and subsequently the nested State:
```
{
    "name": "Bundaleer Rainforest Gardens",
    "street_number": 59,
    "street_name": "Bundaleer St",
    "phone": "0733741360",
    "email": "hello@bundaleer.com",
    "description": null,
    "cost_per_head": 190,
    "min_guests": 80,
    "max_guests": 200,
    "city": {
        "state": {
            "name": "South Australia"
        },
        "name": "Kingsford",
        "postcode": 5118
    }
}
```

* The Wedding Model

```
# SQLAlchemy creates table structure with columns and data types
class Wedding(db.Model):
    # Renames table to plural based on convention
    __tablename__ = 'weddings'

    id = db.Column(db.Integer, primary_key=True)
    date_of_wedding = db.Column(db.Date())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    user = db.relationship('User', back_populates='wedding') # No cascade delete as when a wedding entry is deleted, the user shouldn't be deleted.
    venue = db.relationship('Venue', back_populates='weddings') # No cascade delete as when a wedding entry is deleted, the venue shouldn't be deleted.


# JSON (de)serialization with Marshmallow
class WeddingSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['f_name', 'l_name'])
    venue = fields.Nested('VenueSchema', only=['name', 'city'])
    date_of_wedding = fields.Date()
    venue_id = fields.Integer()

    class Meta:
        fields = ('id', 'date_of_wedding', 'user', 'venue_id', 'venue')
        ordered = True # Orders keys in the same order as above
```
The wedding model contains two foreign keys, user_id and venue_id, relating to the primary keys of the user and venue models respectively. The difference is that it is a one to one relationship between user and wedding, whereas it's a one to many relationship between venue and wedding, as described previously. No cascade delete was set up in `db.relationship` because when a wedding entry is deleted, both the user and the venue data should still remain. Both the user and the venue fields are nested inside the wedding schema, so we can see them when we return a wedding entry in JSON; subsequently the city and state are nested inside the venue:
```
{
    "date_of_wedding": "2024-05-12",
    "user": {
        "f_name": "Sally",
        "l_name": "Smith"
    },
    "venue": {
        "name": "Quamby Estate",
        "city": {
            "state": {
                "name": "Tasmania"
            },
            "name": "Hagley",
            "postcode": 7292
        }
    }
}
```

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

* Dhruv, S. (2019). Pros and Cons of using PostgreSQL for Application Development. [online] Aalpha. Available at: https://www.aalpha.net/blog/pros-and-cons-of-using-postgresql-for-application-development.

* LinkedIn. (2023). What are the benefits and drawbacks of using ORM for complex queries and aggregations? [online] Available at: https://www.linkedin.com/advice/0/what-benefits-drawbacks-using-orm-complex-queries#:~:text=One%20of%20the%20main%20benefits.

* Tuama, D.Ó. (2022). Object Relational Mapping: What is an ORM? [online] Code Institute Global. Available at: https://codeinstitute.net/global/blog/object-relational-mapping.

* Abba, I.V. (2022). What is an ORM – The Meaning of Object Relational Mapping Database Tools. [online] freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools.

* TutorialsPoint. (n.d.). SQLAlchemy Tutorial. [online] Available at: https://www.tutorialspoint.com/sqlalchemy/index.html.

* Mwaura. (2021). Object validation and conversion with Marshmallow in Python. [online] Available at: https://circleci.com/blog/object-validation-and-conversion-with-marshamallow.

* Psycopg. (2021). Psycopg – PostgreSQL database adapter for Python — Psycopg 2.9.6 documentation. [online] Available at: https://www.psycopg.org/docs/index.html.

* PyPI. (2023). python-dotenv. [online] Available at: https://pypi.org/project/python-dotenv/#getting-started.

* GeeksforGeeks. (2023). Password Hashing with Bcrypt in Flask. [online] Available at: https://www.geeksforgeeks.org/password-hashing-with-bcrypt-in-flask.

* Flask-JWT-Extended. (n.d.). Basic Usage — flask-jwt-extended 4.5.2 documentation. [online] Available at: https://flask-jwt-extended.readthedocs.io/en/stable/basic_usage.html.