# 🚀 My First FastAPI Project

This is my first FastAPI project. The project allows users to create blogs and authenticate before showing or changing or creating any blog.

# 🚀 Getting Started

1. Clone the repository
2. Create a virtual environment using **virtualenv env**
3. Activate the environment using `source env/bin/activate`
4. Install the requirements using `pip install -r requirements.txt`
5. Run the server using `uvicorn main:app --reload`
6. Run **http://127.0.0.1:8000/docs** in your browser
7. Authenticate by clicking the **Authorize** button and providing your credentials in the login form **(username: string, password: string)**
8. Once authenticated, you will be able to create and show blogs using the **/blogs** endpoint
