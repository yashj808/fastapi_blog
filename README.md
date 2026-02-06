# FastAPI Blog

A simple blog application built with FastAPI.

## Features

*   View all blog posts
*   View a single blog post
*   View all posts by a user
*   API to get all blog posts
*   API to get a single blog post
*   API to get all posts by a user
*   API to create a user
*   API to create a post
*   API to update a post

## Getting Started

### Prerequisites

*   Python 3.13
*   `pipenv`

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/fastapi_blog.git
    ```
2.  Install the dependencies:
    ```bash
    pipenv install
    ```

### Running the application

To run the application, use the following command:

```bash
pipenv run uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

*   `GET /api/posts/`: Get all blog posts.
*   `GET /api/posts/{post_id}`: Get a single blog post by its ID.
*   `POST /api/posts/`: Create a new blog post.
*   `PUT /api/posts/{post_id}`: Update a blog post.
*   `GET /api/users/{user_id}`: Get a user by their ID.
*   `POST /api/users/`: Create a new user.
*   `GET /api/users/{user_id}/posts`: Get all posts by a user.

## Project Structure

```
├── .gitignore
├── blog.db
├── database.py
├── main.py
├── models.py
├── Pipfile
├── Pipfile.lock
├── README.md
├── schemas.py
├── snippets.txt
├── media
│   └── profile_pics
├── static
│   ├── css
│   │   └── main.css
│   ├── icons
│   │   ├── favicon.ico
│   │   ├── icon-512.png
│   │   └── icon.svg
│   ├── js
│   │   └── utils.js
│   └── profile_pics
│       └── download.jpg
│   └── site.webmanifest
└── templates
    ├── error.html
    ├── home.html
    ├── layout.html
    ├── post.html
    └── user_posts.html
```

## Technologies Used

*   [FastAPI](https://fastapi.tiangolo.com/)
*   [SQLAlchemy](https://www.sqlalchemy.org/)
*   [Python 3.13](https://www.python.org/)
*   [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
*   [Pipenv](https://pipenv.pypa.io/en/latest/)
