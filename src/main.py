from fastapi import FastAPI

from routes.users import user_routes
from routes.superitendences import superitendence_routes

app = FastAPI(title="SIMOVE")

# Routes
app.include_router(user_routes)
app.include_router(superitendence_routes)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=3333, reload=True)