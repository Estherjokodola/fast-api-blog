from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Hello World"}

posts: list[dict] = [ 
    {
        "id": 1,
        "author": "Corey Schafer",
        "content": "FastAPI is awesome",
        "title": "This framework is really easy to use and super fast",
        "date_posted":"April 20, 2025",
        
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "content": "I love FastAPI",
        "title": "FastAPI is the best framework for building APIs",
        "date_posted":"April 21, 2025",
    }
]

@app.get("/posts", response_class = HTMLResponse, include_in_schema=False)
@app.get("/", response_class = HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/api/posts")
def get_posts():
    return posts