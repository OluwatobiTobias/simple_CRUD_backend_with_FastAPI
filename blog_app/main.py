from fastapi import FastAPI, Query, Depends
from typing import Dict
import uvicorn

app = FastAPI()

@app.get('/', tags=['Root'])
def home_page() -> Dict[str, str]:
    return {'home_page': 'Welcome to this Blog Application'}

@app.get('/bye')
def bye_page() -> Dict[str, str]:
    return {'bye_page': 'BYE!!!'}

def start_application():
    # if __name__ == "__main__":
        from sys import argv

        print(argv)
        port if (port := int(argv[1])) else (port := 8000)
        uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
    
    # else:
    #     print('is not running file directly')