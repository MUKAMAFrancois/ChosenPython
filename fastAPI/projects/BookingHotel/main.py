from fastapi import FastAPI
from routers.users_routes import userRouter





description = """This is a simple API for booking hotel. 
It has the following features:

## User
- Register
- Login
- Book a Hotel Room
- View User Profile
- Update User Profile
- Delete User Profile
- Password Change
- Password Reset
- Logout

- Write Hotel Testimonial
- View Hotel Testimonials
- Delete Hotel Testimonial [by User who wrote it]
-Message the To the Admin
-Subscribe to the Newsletters


## Hotel
- Add Hotel [by Admin]
- Update Hotel [by Admin]
- Delete Hotel [by Admin]
- View Hotel Details [by User]
- View All Hotels [by User]
- Search Hotel [by User]
- Book Hotel [by User]

## Location
- Hotels by Location [by User]
- Add Location [by Admin]
- Update Location [by Admin]
- Delete Location [by Admin]
- View Location [by User]


"""

app = FastAPI(
    title="API for Booking Hotel",
    description=description,
    summary="API for Booking Hotel",
    version="1.0.0"
)



app.include_router(userRouter)