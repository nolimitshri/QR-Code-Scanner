import pyqrcode # firstly install the module "pip install pyqrcode"
from pyqrcode import QRCode 

web_url = "https://nolimitshri.github.io/styledCV/" # your link here in the double quotes..

url = pyqrcode.create(web_url)

url.svg("styled.svg", scale = 8) # you can save it as styled.png too!!
