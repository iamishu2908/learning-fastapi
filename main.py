from fastapi import FastAPI
from router import blog_get
from router import blog_post
from fastapi import Request
from exceptions import StoryException
from fastapi.responses import JSONResponse

from db import models
from db.database import engine
from router import user
from router import article

# we use this line to start our server and to define our path(@app.get)
app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

#attaching function to an endpoint
@app.get('/')
def index():
    return {'message' : "Hello World !"}

@app.exception_handler(StoryException)
def story_exception_handler(request:Request,exp: StoryException):
    return JSONResponse(
        status_code = 418,
        content = {'detail' : exp.name}
    )

models.Base.metadata.create_all(engine)
