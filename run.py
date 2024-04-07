#pylint: disable:syntax-error
from src.main.server.server import app

@app.get('/hello-world')
def hello_world():
    return True
