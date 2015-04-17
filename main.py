import pygtk
pygtk.require('2.0')
import gtk
from pyshorteners.shorteners  import Shortener

# get the clipboard
clipboard = gtk.clipboard_get()

#read clipboard for the text copied
url_original = clipboard.wait_for_text()

try:
	shortener = Shortener('TinyurlShortener')
	url = format(shortener.short(url_original))
	# set the clipboard data as shortened url
	clipboard.set_text(url)
except:
	clipboard.set_text(url_original)
# Storing short url to clipboard
clipboard.store()