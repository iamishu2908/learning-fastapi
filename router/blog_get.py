from fastapi import APIRouter
from enum import Enum
from typing import Optional
from fastapi import status,Response

router = APIRouter(
    prefix = '/blog',
    tags = ['blog']
)


# summary and description
@router.get('/all', 
         summary = 'Retrieve all blogs', \
         description = 'this api fetches all blogs.',\
         response_description = "the list of available blogs are found")
def get_all_blogs(page=1):
    return {'message' : f'it has {page} pages.'}
    
# description as docstring
@router.get('/{id}/comments/{comment_id}',tags = ['comment'])
def get_comment(id:int,comment_id:int,valid:bool=True,username:Optional[str] = None):
    """
    Simulates retrieving a comment of a blog
    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **bool** optional query parameter
    - **username** optional query parameter
    """
    return {'message' : f'blog_id-> {id}, comment_id -> {comment_id}, valid : {valid}, username:{username}'}

#optional parameters

@router.get('/all')
def get_blogs(page = 1, pagesize : Optional[int] = None):
    return {'message' : f'There are {pagesize} pages on page {page}'}
#query parameters(defined values)

@router.get('/all')
def get_blogs(page = 1, pagesize = 10):
    return {'message' : f'There are {pagesize} pages on page {page}'}

# predefined values
class BlogType(str,Enum) :
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/type/{type}')
def get_blog_type(type:BlogType):
    return {'message' : f'Blog type {type}'}

