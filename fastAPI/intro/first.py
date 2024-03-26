# FastAPI is a modern, fast (high-performance),
# web framework for building APIs with Python 3.7+. 
# It's designed to be easy to use, 
#     fast to develop with, and capable of handling high loads



# UVicorn is the ASGI server that FastAPI runs on. 
# ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to 
# WSGI (Web Server Gateway Interface) and is designed to 
# support asynchronous Python web frameworks. UVicorn allows FastAPI to handle
# high levels of concurrency by running asynchronously.

# Pydantic is a data validation and settings management library
# for Python. It's heavily used in FastAPI for request and response
# validation. Pydantic helps ensure that data passed to and 
# from your API endpoints is correct and properly formatted.


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}


# To run the server, use the following command:
# uvicorn first:app --reload


@app.get("/about")
def about_us():
    return {"message": "This is the about page!"}