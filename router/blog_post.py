from typing import Optional,List,Dict
from fastapi import APIRouter, Query,Body,Path
from pydantic import BaseModel

router = APIRouter(
    prefix = '/blog',
    tags = ['blog']
)

class Image(BaseModel):
    url:str
    alias:str

class BlogModel(BaseModel): # inheriting basemodel 
    title : str
    content : str
    published : Optional[bool]
    nb_comments: int
    tags:List[str] = []
    metadata : Dict[str,str] = {'key1':'val1'}
    image:Optional[Image] = None
    
@router.post('/new/{id}')
def create_blog(blog : BlogModel, id:int, version : int =1):
    return {'id':id,'version':version,'data':blog}

#parameter metadata

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int, 
                   comment_title : int = Query(
    None,
    title='Title of the comment',
    description = 'some desc',
    alias = 'CommentTitle',deprecated = True),
    content:str = Body(
        ...,
        min_length=10,
        max_length=12,
        regex='^[a-z\s]*$'),
    v : Optional[List[str]] = Query(None),
    comment_id : int = Path(None,gt=5,le=10)
    ):

    return {
        'blog' : blog,
        'id' : id,
        'comment_title' : comment_title,
        'content' : content ,
        'version' : v,
        'comment_id': comment_id
    }

def req_functionality():
    return {'message': 'learning fast api wow'}
