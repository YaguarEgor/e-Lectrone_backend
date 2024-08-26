from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from feedbacks.router import router as feedback_router
from tutors.router import router as tutor_router


#запускать на 8003 порту!!!!!!!

app = FastAPI()

@app.get("/hi")
async def hello():
    return "hello guys"


app.include_router(feedback_router)
app.include_router(tutor_router)

#CORS
#region
origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=[],
)
#endregion
