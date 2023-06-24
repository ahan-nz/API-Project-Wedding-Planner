# T2A2 - API Webserver Project
## By Alicia Han
---

### Installation Instructions

psql postgres
create database wedding_planner;
\c wedding_planner
create user planner_dev with password 'wedding123';
grant all privileges on database wedding_planner to planner_dev;


### R1 Identify the problem you are trying to solve with this app

The purpose of this app is to simplify and organise the task of wedding planning. The aim is make this often stressful task a better experience by giving brides and grooms a starting point on brainstorming and planning for their big day, and having the details all in one place; the app can also be used by professional wedding planners to track vendors for their clients. For the purposes of this assignment the scope has been limited, however there is potential to scale and add more features such as catering or florists.

### R2 Why is it a problem that needs solving?

Wedding planning can be a huge and daunting task with many variables, and most brides and grooms have little experience with event planning. There are a multitude of choices such as venues, catering and vendors, which can be difficult to track. In addition, wedding planners can be very costly, which can be unattainable for many couples who may be stretching their budget for the wedding. 

### R3 Why have you chosen this database system. What are the drawbacks compared to others?

PostgreSQL is a widely-adopted object-relational DBMS that I chose due to it's many advantages. Firstly it is open source and free to use, which keeps the initial cost small (if any). As a beginner in the field, it has a lower learning curve compared to some other database systems. In addition, as mentioned above, it is widely used in the industry and is supported by a large community with extensive forum discussions and documentation, hence there is help readily available if there are any issues. 

Despite being free to use, PostgreSQL is very feature-rich. It is highly extensible, which means new functions, data types, etc, can be added. There is a wide range of libraries and tools available for developers and is supported across all the common platforms including MacOS, Linux, and Windows (PostgreSQL, 2020). It is very scalable, and used with relational databases that can store large datasets in tables, utilising transactional Data Definition Language to easily implement mdifications to the database with minimal disruption to the framework. Although my application won't have a big database for this assignment, there is the potential to grow. It is also helpful to have the data in a rigid schema for ease of access and also to establish clear relationships between each entity.

PostgreSQL is ACID compliant, which stands for atomicity, consistency, isolation and durability. Atomacity refers to how every operation has to succeed for the transaction to succeed, avoiding unintential results from partial transactions. Consistency is sticking to the database constraints and isolation means transactions, even if happening at the same time, won't interfere with one another. Finally, durability refers to an up to date database once a transaction happens (MongoDB, 2023). This ensures a reliable database for my app that supports multiple users and high transactional loads if needed.

Last but not least, PostgreSQL is secure, so our users' details are better protected, user accounts can be authenticated and also set up with varying permission at handling the data.

Some of the drawbacks include some open source apps support MySQL but not PostgreSQL, and PostgreSQL also has slower performance metrics than MySQL (Dhruv, 2019) as it starts from the first row of a table in a relationship database and reads it sequentially. However these aren't as important as PostgreSQL being better at executing complex queries for this application, and that it's free to use. MySQL is also only ACID compliant in certain conditions. 

One could argue that PostgreSQL is also less flexible, compared to say MongoDB, in the sense that a table in a relational database cannot have extra fields outside of the set schema. However this is unlikely to be an issue with the limited entities that we have in this application.

### R4 Identify and discuss the key functionalities and benefits of an ORM

Object relational mapper
Relational databases typically uses a querying language called SQL to manipulate the structure and data in our database. With ORM, the SQL is generated for us behind the scenes.

Benefits:
* Works with Python objects in this case, we don't have to write SQL
* Allows you to switch your database easily
* You can control the structure of your database from your code, which can be managed by a revision control system like Git or Subversion.
* Supports multiple database platforms e.g. if you're selling your API code for distribution in on-premises soluions.

### R5 Document all endpoints for your API

### R6 ERD

### R7 Detail any third party services that your app will use

### R8 	Describe your projects models in terms of the relationships they have with each other



### R9 Discuss the database relations to be implemented in your application



### R10 Describe the way tasks are allocated and tracked in your project

I initially brainstormed ideas for a project on paper, and chose the most practical one to propose on Discord for educator approval.

I also formed a rough idea of the entities and relationships during this, which acted as the basis for my ERD.

* User Stories

This is where I started to think about the end goals of the application, from the point of view of the end user to improve customer satisfaction. I created several user stories from the point of view of the user, which is the bride/groom/wedding planner in this case. These will help with the planning stage of the application and ensure I start with the end in mind. My user stories were as follows:

1. As a bride/groom/wedding planner, I want to be able to create a user profile with ease and have my information secure.

2. As a bride/groom/wedding planner, I want to be able to create, read, update or delete a wedding event. I don't want other general users to be able to modify this information.

3. As an admin of the app, I want to have be able to perform CRUD on all models.

4. As a bride/groom/wedding planner, I want to be able to add/modify/delete guests and their information, such as contact details and whether or not they have RSVP'ed.

5. As a bride/groom/wedding planner, I want to be able to create, read, update or delete potential venues and it's information, like address, contact details, and costs.

I am utilising Trello to help me track tasks throughout this project, with lists based on a Kanban board template, including:

* Backlog

This is a list of tasks that I have yet to start on. It helps me to plan and clarify the exact tasks that I need to complete. This will also include tasks that may be out of scope for this assignment that I can work on in future, including adding other vendors such as florists or wedding dress fittings.

* In Progress

These are the tasks that I am currently working on, it's useful not only for tracking my progress but also to make sure I don't have too many cards in this list at the same time. It would also be useful if I were working in a team so we are update to date with each others' progress.

* Review

These are the tasks that I have completed but yet to finalise. For example my ERD card went here once I finished the initial plan, but it may be subject to change. It may also include code that I've written but yet to be tested fully.

* Done

These are tasks that I have completed and no longer need to revisit.

The Trello board allows me to grasp the big picture of the progress of my assignment quickly.

### References

* PostgreSQL Documentation. (2020). 1. What Is PostgreSQL? [online] Available at: https://www.postgresql.org/docs/current/intro-whatis.html.

* MongoDB. (2023). What Does ACID Compliance Mean? | An Introduction. [online] Available at: https://www.mongodb.com/databases/acid-compliance#:~:text=Well%2C%20ACID%20stands%20for%20atomicity.

* Dhruv, S. (2019). Pros and Cons of using PostgreSQL for Application Development. [online] Aalpha. Available at: https://www.aalpha.net/blog/pros-and-cons-of-using-postgresql-for-application-development/.

