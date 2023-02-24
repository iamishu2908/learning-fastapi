from typing import Optional,List
from fastapi import APIRouter, Query,Body
from pydantic import BaseModel

router = APIRouter(
    prefix = '/blog',
    tags = ['blog']
)

class BlogModel(BaseModel):
    title : str
    content : str
    published : Optional[bool]
    nb_comments: int
    
@router.post('/new/{id}')
def create_blog(blog : BlogModel, id:int, version : int =1):
    return {'id':id,'version':version,'data':blog}

#parameter metadata

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int, 
                   comment_id : int = Query(
    None,
    title='Id of the comment',
    description = 'some desc',
    alias = 'CommentID',deprecated = True),
    content:str = Body(
        ...,
        min_length=10,
        max_length=12,
        regex='^[a-z\s]*$'),
    v : Optional[List[str]] = Query(None)
    ):

    return {
        'blog' : blog,
        'id' : id,
        'comment_id' : comment_id,
        'content' : content ,
        'version' : v
    }
