from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from models import Song


app = FastAPI()
songs: list[Song] = []
templates = Jinja2Templates('HW5/templates')


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'songs': songs})


@app.get('/music/{id}', response_class=HTMLResponse)
async def get_song(request: Request, id: int):
    filtered_songs = [song for song in songs if song.id == id]
    if not filtered_songs:
        song = None
    else:
        song = filtered_songs[0]
    return templates.TemplateResponse('song.html', {'request': request, 'song': song})


@app.get('/author/{author}', response_class=HTMLResponse)
async def get_author(request: Request, author: str):
    filtered_author = [song for song in songs if song.author == author]
    return templates.TemplateResponse('author.html', {'request': request, 'songs': filtered_author})


@app.get('/genre/{genre}', response_class=HTMLResponse)
async def get_genre(request: Request, genre: str):
    filtered_genre = [song for song in songs if song.genre == genre]
    return templates.TemplateResponse('genre.html', {'request': request, 'songs': filtered_genre})


@app.post('/music/')
async def create_song(song: Song):
    songs.append(song)
    return song


@app.put('/music/{id}')
async def update_song(id: int, new_song: Song):
    for song in songs:
        if song.id == id:
            song.title = new_song.title
            song.author = new_song.author
            song.description = new_song.description
            song.genre = new_song.genre
            return {'updated': True, 'song': song}


@app.delete('/music/{id}')
async def delete_song(id: int):
    for song in songs:
        if song.id == id:
            songs.remove(song)
            return {'deleted': True, 'song': song}
