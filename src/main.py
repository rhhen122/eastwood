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
def favicon(filelocfavicon):
    fortext = f"<link rel='icon' type='image/x-icon' href='{filelocfavicon}'>"
    app(fileloc, fortext, False)
def title(title):
    fortext = f"<title>{title}</title>"
    app(fileloc, fortext, False)
def metadata(metadata):
    fortext = f"<meta name='description' content='{metadata}'>"
    app(fileloc, fortext, False)
def ulist(_id, cl, ot):
    fortext = f"<ul id='{_id}' class='{cl}' {ot}>"
    app(fileloc, fortext, False)
def ulistclose():
    app(fileloc, "</ul>", False)
def input(placeholder, _id, cl, ot):
    fortext = f"<input placeholder='{placeholder}' id='{_id}' class='{cl}' {ot}>"
    app(fileloc, fortext, False)
def button(text, _id, cl, ot):
    fortext = f"<button id='{_id}' class='{cl}' {ot}>{text}</button>"
    app(fileloc, fortext, False)
def link(text, href, _id, cl, ot):
    fortext = f"<a href='{href}' id='{_id}' class='{cl}' {ot}>{text}</a>"
    app(fileloc, fortext, False)
def hr():
    app(fileloc, '<hr>', False)

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

