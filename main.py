from fasthtml.common import (
    FastHTML, Link, Div, serve, FileResponse
)
import another_page


# Using the FastHTML class rather than 
# the fast_app function, removes Pico CSS
app = FastHTML(hdrs=Link(rel="stylesheet", href="app.css", type="text/css"))
rt = app.route

# Tell fasthtml which 'app.css' to use
# This function takes any request for a file, adds the public 
# folder to the filename, and returns it as a file
@rt("/{fname:path}.{ext:static}")
def get(fname:str, ext:str): 
    return FileResponse(f'public/{fname}.{ext}')


@rt('/')
def get():
    return another_page.content

serve()