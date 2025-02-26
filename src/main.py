from fastapi import FastAPI

app = FastAPI(title="SIMOVE")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=3333, reload=True)