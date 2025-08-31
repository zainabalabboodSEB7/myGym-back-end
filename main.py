from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.teas import router as TeasRouter
from controllers.comments import router as CommentsRouter
from controllers.users import router as UsersRouter
from controllers.category import router as CategoryRouter
from controllers.sessions import router as SessionRouter
from controllers.reviews import router as ReviewRouter

app = FastAPI()

app.include_router(TeasRouter, prefix='/api')
app.include_router(CommentsRouter, prefix='/api')
app.include_router(UsersRouter, prefix='/api')
app.include_router(CategoryRouter, prefix='/api')
app.include_router(SessionRouter, prefix='/api')
app.include_router(ReviewRouter, prefix='/api')

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    # Later, add your deployed frontend origin, e.g.:
    # "https://your-frontend.example.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # Which sites can call this API
    allow_methods=["*"],       # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],       # Allow all headers (e.g., Content-Type, Authorization)
    # NOTE: We are NOT using credentials in this simple lesson,
    # so we are not setting allow_credentials.
)

@app.get("/health")
def health_check():
    return {"ok": True}

@app.get('/')
def home():
    # Hello world function
    return {'message': 'Hello World!'}
