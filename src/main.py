from fastapi import FastAPI

app = FastAPI(
    title='FISCALIZA',
    version='0.1.0',
)

@app.get('/')
async def hello_world():
    return {'message': 'hello world'}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app=app,
        host='localhost',
        port=8000,
    )
