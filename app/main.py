from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from . import models, database



app = FastAPI()

# 1. Setup Static Files (for CSS/JS/Images)
# Place your htmx.min.js in app/static/
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 2. Setup Jinja2 Templates
templates = Jinja2Templates(directory="app/templates")

# --- WEB ROUTES (Serving HTML) ---

# --- WEB ROUTES (Serving HTML) ---

@app.get("/", response_class=HTMLResponse)
async def index(request: Request, db: Session = Depends(database.get_db)):
    # Correct order: name of template, then context dictionary
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={}  # Add data here later (e.g., "incidents": incidents)
    )

@app.get("/coming-soon/test", response_class=HTMLResponse)
async def placeholder(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="placeholder.html", 
        context={}
    )
