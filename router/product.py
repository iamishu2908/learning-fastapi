from typing import List, Optional
from fastapi import APIRouter, Cookie,Header
from fastapi.responses import Response,HTMLResponse,PlainTextResponse


router = APIRouter(
  prefix='/product',
  tags=['product']
)

products = ['watch','camera','phone']

@router.get('/all')
def get_all_products():
    #return products
    data = " ".join(products)
    response = Response(content=data, media_type = "text/plain")
    response.set_cookie(key = "test_cookie", value = "test_cookie_value")
    return response

@router.get('/withheader')
def get_products(
  response: Response,
  custom_header: Optional[List[str]] = Header(None),test_cookie:Optional[str] = Cookie(None)
  ):
    
  if custom_header:
    response.headers['custom_response_header'] = " and ".join(custom_header)
  return {
    'data': products,
    'custom_header': custom_header,
    'my_cookie' : test_cookie
  }

    
@router.get('/{id}', responses = {
    200:{
    "content":{
    "text/html" : {
    "example":"<div>Product</div>"
    }
    },
    "description" : "returns the html for an object"
    },404:{
    "content":{
    "text/plain" : {
    "example":"<div>Product not available! </div>"
    }
    },
    "description" : "a cleartext error message"
    }
})
def get_product(id:int):
    if id > len(products):
        out = "Product not available"
        return PlainTextResponse(status_code=404 ,content = out, media_type = "text/plain")
    else:
      product = products[id]
      out = f"""
      <head>
        <style>
        .product {{
        width:500px;
        height:30px;
        border: 2px inset green;
        background-color: lightblue;
        text-align: center;
        }}
        </style>
      </head>
      <div class="product">{product}</div>

      """
      return HTMLResponse(content=out,media_type="text/html")
