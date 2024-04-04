from fastapi import APIRouter


userRouter=APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)




@userRouter.get("/")
def test():
    return {"message":"Hello World"}