import uvicorn
from app.fastApp import app

if __name__ == '__main__':
    uvicorn.run(app)