from src.main import *
from init import *

init(fileloc)

style('style.css')
title('EastWood')

header('Eastwood - SSG', '', 'head', '', '1'); hr()

text("""
EastWood is a SSG (Static Site generator) built in Python(3)!

I wrote it in Emacs (The best editor) and tested it with the amazing buil script!
""")

button('Open README.md', '', '', """onclick="window.location.href = 'https://github.com/rhhen122/eastwood/blob/master/README.md'" """)

end(fileloc)
