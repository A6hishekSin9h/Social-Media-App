
Link: https://social-media-backend-5fo6.onrender.com/docs

** Note: The website takes some time to load (appx ~ 30-40 secs) as it is hosted under a free instance. **

# Social Media App Backend
Steps to try it out:
1. create your user account using "create user".
2. login using the credentials.
3. create, update and delete your posts.
4. you can also vote/unvote others post by sending 1 and 0.

This is the backend component of a social media app built using Python and FastAPI. It utilizes PostgreSQL as the database server and SQLAlchemy for performing database operations. The app includes user authentication and authorization using JWT tokens, as well as a voting feature where users can vote or unvote a post.

Features
* User registration: New users can sign up for an account by providing their details such as email, and password.
* User login: Registered users can log in to their accounts using their credentials.
* JWT token generation: Upon successful login, the backend generates a JWT token that will be used for subsequent authenticated requests.
* User profile: Each user has a profile that contains information such as their userID, email, and other optional details.
* Post creation: Users can create posts by providing a title and content for their posts.
* Post retrieval: Users can retrieve a list of all posts or view individual posts.
* Post update and deletion: Users can update or delete their own posts.
* Voting: Users can vote or unvote a post to express their preference.
  
Technologies Used
* Python: Programming language used for the backend development.
* FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
* PostgreSQL: An open-source relational database management system.
* SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
* JWT: JSON Web Tokens are used for user authentication and authorization.
  
Prerequisites
To run this project, you'll need the following installed on your machine:

* Python 3.7+
* PostgreSQL server
* pip package manager

Configuration

The configuration for the project can be found in the config.py file. You may need to update the following settings:

* DATABASE_URL: The connection URL for your PostgreSQL database.
* SECRET_KEY: A secret key used for JWT token generation.

Acknowledgments
* The FastAPI and SQLAlchemy communities for their excellent libraries.
* The PostgreSQL community for providing a reliable database system.
* JSON Web Tokens for secure authentication and authorization.
