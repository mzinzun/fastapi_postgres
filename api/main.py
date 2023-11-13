from fastapi import FastAPI
from router.routes import router

app = FastAPI()
app.include_router(router)

@app.get('/')
def test():
    return {'message': 'FastAPI running'}
