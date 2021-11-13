from fastapi import FastAPI, File, UploadFile
from html2text import HTML2Text

from models.mdhtml import HTMLStr

app = FastAPI()

@app.get('/')
def get_root():
    return {'Hello': 'Markdown'}

@app.post('/stringtomd/')
async def HTMLStringToMarkdown(item:HTMLStr):
    h = HTML2Text(baseurl="")
    try:
        mdata = h.handle(item.html)
        return {'markdown': mdata}
    except:
        return {'error': 'Failed to parse string'}

@app.post('/htmltomd/')
async def HTMLFileToMarkdown(file: UploadFile = File(...)):
    h = HTML2Text(baseurl="")
    try:
        contents = await file.read()
        html = contents.decode('utf-8', 'ignore')
        mdata = h.handle(html)
        return {'markdown': mdata.encode('utf-8')}
    except:
        return {'error': 'Failed to parse file'}