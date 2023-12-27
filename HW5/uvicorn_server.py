import uvicorn


if __name__ == '__main__':
    uvicorn.run('main:app', port=80, reload=True)