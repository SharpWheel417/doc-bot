from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, CallbackContext, filters
import src.processing.dirs

from config import BOT_TOKEN

from src.controller.document import handle_css, handle_document, handle_html, handle_js

from src.controller import document

from src.controller.message import handle_message
from src.controller.command import start
from src.parsing.weather import send_weather_for_all

application = ApplicationBuilder().token(BOT_TOKEN).build()

# application.add_handler(CallbackQueryHandler(button_callback))


### COMMAND
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

weather_handler = CommandHandler('weather', send_weather_for_all)
application.add_handler(weather_handler)


### DOC
doc_handler = MessageHandler(filters.Document.DOC, document.handle_document)
application.add_handler(doc_handler)

### DOX
docx_handler = MessageHandler(filters.Document.DOCX, document.handle_document)
application.add_handler(docx_handler)

### HTML
html_handler = MessageHandler(filters.Document.MimeType("text/html"), handle_html)
application.add_handler(html_handler)

### CSS
css_handler = MessageHandler(filters.Document.MimeType("text/css"), handle_css)
application.add_handler(css_handler)

### JS
js_handler = MessageHandler(filters.Document.MimeType("text/javascript"), handle_js)
application.add_handler(js_handler)

# photo_handler = MessageHandler(filters.PHOTO, handle_photo)
# application.add_handler(photo_handler)


### TEXT
message_handler = MessageHandler(filters.TEXT, handle_message)
application.add_handler(message_handler)

application.run_polling()