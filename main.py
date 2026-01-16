from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Yash Jogdand",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False) #The include in schema hides the http endpoint from the docs, so that people visiting the docs don't see the particular endpoint
def home():
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/api/posts/")
def get_posts():
    return posts

