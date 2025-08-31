from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from controllers.users import router as UsersRouter
from controllers.category import router as CategoryRouter
from controllers.sessions import router as SessionRouter
from controllers.reviews import router as ReviewRouter

app = FastAPI()

app.include_router(UsersRouter, prefix='/api')
app.include_router(CategoryRouter, prefix='/api')
app.include_router(SessionRouter, prefix='/api')
app.include_router(ReviewRouter, prefix='/api')

