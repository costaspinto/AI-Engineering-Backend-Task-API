from fastapi import FastAPI

app = FastAPI(title="AI Engineering Task API")


@app.get("/")
def root():
    return {"message": "Task API is running"}