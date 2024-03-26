
from typing import List
from uuid import UUID, uuid4
from models import User,UserRole,Gender,Region
from fastapi import FastAPI



application = FastAPI()


db:List[User] = [
    User(
       # id=UUID("e19779e-3db2-4ace-ad5c-5d6f976e7b72"),
        id=uuid4(),
        first_name="John",
        last_name="Doe",
        middle_name="Smith",
        telephone_number="1234567890",
        gender=Gender.male,
        userRole=UserRole.user,
        location=[Region.north,Region.south]
    ),
    User(
        #id=UUID("226aa514-7c76-4ddc-90b4-06945516378a"),
        id=uuid4(),
        first_name="Jane",
        last_name="Doe",
        middle_name="Smith",
        telephone_number="1234567890",
        gender=Gender.female,
        userRole=UserRole.student,
        location=[Region.east,Region.west]
    )
]


#get all users
@application.get("/api/v1/users")
async def get_all_users():
    # result = await db
    # return result

    return {"Users": db}


# Get a user by ID
@application.get("/api/v1/users/{user_id}")
async def get_user_by_id(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return {"User": user}
    return {"message": "User not found"}



# Create a new user
@application.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {
        "message": "User created successfully!",
        "User": user
            }

# Update a user
@application.patch("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user: User):
    for u in db:
        if u.id == user_id:
            u.first_name = user.first_name
            u.last_name = user.last_name
            u.middle_name = user.middle_name
            u.telephone_number = user.telephone_number
            u.gender = user.gender
            u.userRole = user.userRole
            u.location = user.location
            return {"message": "User updated successfully!", "User": u}
    return {"message": "User not found"}


# Delete a user
@application.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted successfully!"}
    return {"message": "User not found"}


    