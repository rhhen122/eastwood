# Eastwood

`Eastwood` is a SSG (Static Site Generator) written in Python(3) Built on stream in my lounge using `E-Macs` and ducttape (Google AI)

## Usage
Its syntax is simple. Let me give you a example:
```python
# An Example with the 'text()' func
text('Heres my text! This will be rendered when im ran!')
```
Heres how configuring and getting it start up works:
```python
# First we want to import things from these files!
from src.main import * # This one contains the functions that the user cals to to make a element on the website!
from init import * # This one contains configuration items

init(fileloc)

text('A text element has wildly appered!')

end(fileloc)
```
