# COPYRIGHT: Roky Henderson / Rhhen

from init import *

# Append function defenition
def app(fileloc, content, writefirst):
    if writefirst == True:
        with open(fileloc, "w") as file:
            file.write("")
    with open(fileloc, "a") as file:
        file.write(f"{content}\n")

# Tags
def header(text, _id, cl, ot, wh):
    fortext = f"""
<h{wh} id='{_id}' class='{cl}' {ot}>
    {text}
</h{wh}>
    """
    app(fileloc, fortext, False)
def text(text):
    fortext = f"<p>{text}</p>"
    app(fileloc, fortext, False)
def style(filelocstyle):
    fortext = f"<link rel=stylesheet href={filelocstyle}>"
    app(fileloc, fortext, False)
def raw(text):
    app(fileloc, text, False)
def img(src, height, width, _id, cl, ot):
    fortext = f"<img src='{src}' height='{height}' width='{width}' id='{_id}' class='{cl}' {ot}>"
    app(fileloc, fortext, False)
def br():
    app(fileloc, '<br>', False)
def script(filelocscript):
    fortext = f"<script src='{filelocscript}'></script>"
    app(fileloc, fortext, False)
def js(script):
    fortext = f"""
<script>
{script}
</script>
    """
    app(fileloc, fortext, False)
def css(css):
    fortext = f"""
<style>
{css}
</style>
    """
    app(fileloc, fortext, False)

# INIT
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

