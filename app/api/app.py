

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='app/api/templates')

app = FastAPI(title='Lisghts_Recognition')
app.mount("/static", StaticFiles(directory="app/api/static"), name="static")