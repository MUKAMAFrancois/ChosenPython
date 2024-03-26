from fastapi import FastAPI




myapp=FastAPI()


#providing Query parameters which are default values

# @myapp.get("/blogs")
# def all_blogs(limit=10,published:bool=True):
#     if published:
#         return {"data":f"{limit} published blogs from the db"}
#     else:
#         return {"data":f"{limit} blogs from the db"}


#providing Query parameters which are not default values
@myapp.get("/blogs")
def all_blogs(limit:int,published:bool):
    if published:
        return {"data":f"{limit} published blogs from the db"} #http://localhost:8000/blogs?limit=10&published=true
    else:
        return {"data":f"{limit} blogs from the db"}
    


@myapp.get("/blogs/{id}/comments")
def single_blog(id,limit:int=10):
    return {"data":f"blog with id {id} has these comments"}