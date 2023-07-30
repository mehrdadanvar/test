from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.students import router as studentrouter
app = FastAPI()
app.include_router(studentrouter)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

@app.get("/")
async def get_main():
    return {"message":"created"}