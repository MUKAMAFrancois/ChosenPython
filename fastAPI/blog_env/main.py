from fastapi import FastAPI
description="""
This is a simple blog application with CRUD operations

## Blog
You will be able to perform the following operations on the blog:
- Create a blog
- Get all blogs
- Get a blog by Id
- Update a blog
- Delete a blog

## User
You will be able to perform the following operations on the user:
- Register a user
- Login a user
- Get all users
- Get a user by Id
- Update user details
- Delete a user


"""

from blog import models
from blog.database import engine
from blog.routers import blogs,users,authentication



models.Base.metadata.create_all(bind=engine)


app=FastAPI(debug=True,   
             title="Blog API",
    description=description,
    summary="Blog API with crud operations",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
            )

app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(authentication.router)






