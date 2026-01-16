# FastAPI Blog

A simple blog API built with FastAPI.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Install dependencies:**
    This project uses Pipenv for dependency management. To install the required packages, run:
    ```bash
    pipenv install
    ```
3.  **Run the application:**
    To run the development server, use the following command:
    ```bash
    pipenv run uvicorn main:app --reload
    ```
    The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

*   `GET /`: Returns a simple HTML response with the title of the first post.
*   `GET /posts`: Also returns a simple HTML response with the title of the first post.
*   `GET /api/posts/`: Returns a JSON object containing a list of all blog posts.

## Dependencies

*   [FastAPI](https://fastapi.tiangolo.com/)
*   [Uvicorn](https://www.uvicorn.org/)
