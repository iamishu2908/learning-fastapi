from fastapi import FastAPI
from router import blog_get
from router import blog_post

# we use this line to start our server and to define our path(@app.get)
app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

#attaching function to an endpoint
@app.get('/')
def index():
    return {'message' : "Hello World !"}
