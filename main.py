from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory = "templates")
 
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

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})

@app.get("/api/posts")
def get_posts():
     return posts