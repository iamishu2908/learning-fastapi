from fastapi import FastAPI
from router import blog_get

# we use this line to start our server and to define our path(@app.get)
app = FastAPI()
app.include_router(blog_get.router)

#attaching function to an endpoint
@app.get('/')
def index():
    return {'message' : "Hello World !"}
