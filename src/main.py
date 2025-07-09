# COPYRIGHT: Roky Henderson / Rhhen
from init import *
def app(fileloc, content, writefirst):
    if writefirst == True:
        with open(fileloc, "w") as file:
            file.write("")
    with open(fileloc, "a") as file:
        file.write(f"{content}\n")
def header(text, _id, cl, wh):
    fortext = f"""
<h{wh} id='{_id}' class='{cl}'>
    {text}
</h{wh}>
    """
    app(fileloc, fortext, False)
def text(text):
    app(fileloc, text, False)

def init(fileloc):
    inittext = """
<html>
<body>
"""
    app(fileloc, inittext, True)

def end(fileloc):
    endtext = """
</body>
</html>
    """
    app(fileloc, endtext, False)

