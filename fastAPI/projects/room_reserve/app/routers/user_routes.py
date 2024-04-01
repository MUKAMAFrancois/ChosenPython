from fastapi import APIRouter, Depends



router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/test")
def test():
    return {"message":"Hello World"}