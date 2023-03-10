# 🚀 My First FastAPI Project
This is my first FastAPI project. The project allows users to create blogs and authenticate before showing or changing or creating any blog.
<br />
<br />
# 📂 Project Structure
* `main.py`: 🚀 Entry point for the application.
* `app`: 📁 Contains most of the application code.
  * `repository`: 🗃️ Contains database repositories for User and Blog models using **SQLAlchemy**.
  * `routers`: 🛣️ Contains endpoints for User, Blog, and Authentication.
  * `database.py`: 💾 Creates database engine and session, initializes database tables.
  * `hashing.py`: 🔒 Contains function for hashing passwords using **bcrypt**.
  * `models.py`: 📝 Contains models for User and Blog objects defined using **SQLAlchemy**.
  * `oauth2.py`: 🔑 Contains OAuth2 authentication logic for protecting Blog endpoints using **OAuth2PasswordBearer** for authentication.
  * `schemas.py`: 📝 Contains Pydantic schemas for User and Blog objects.
  * `token.py`: 🕰️ Contains logic for generating authentication tokens using **jose**.
<br />

# 🚀 Getting Started
1. Clone the repository
2. Create a virtual environment using **virtualenv env**
3. Activate the environment using `source env/bin/activate`
4. Install the requirements using `pip install -r requirements.txt`
5. Run the server using `uvicorn main:app --reload`
6. Run **http://127.0.0.1:8000/docs** in your browser
7. Authenticate by clicking the **Authorize** button and providing your credentials in the login form **(username: string, password: string)**
8. Once authenticated, you will be able to create and show blogs using the **/blogs** endpoint
<br />

# 🤝 Contributions
Contributions are welcome! If you find any issues or have any suggestions, feel free to create a pull request or submit an issue.
