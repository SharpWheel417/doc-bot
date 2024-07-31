from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, CallbackContext, filters
import os

from config import BOT_TOKEN

from src.controller.document import handle_css, handle_document, handle_html, handle_js
from src.controller.command import start

application = ApplicationBuilder().token(BOT_TOKEN).build()

# application.add_handler(CallbackQueryHandler(button_callback))

start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

doc_handler = MessageHandler(filters.Document.DOC, handle_document)
application.add_handler(doc_handler)

docx_handler = MessageHandler(filters.Document.DOCX, handle_document)
application.add_handler(docx_handler)

html_handler = MessageHandler(filters.Document.MimeType("text/html"), handle_html)
application.add_handler(html_handler)

css_handler = MessageHandler(filters.Document.MimeType("text/css"), handle_css)
application.add_handler(css_handler)

js_handler = MessageHandler(filters.Document.MimeType("text/js"), handle_js)
application.add_handler(js_handler)

# photo_handler = MessageHandler(filters.PHOTO, handle_photo)
# application.add_handler(photo_handler)

# message_handler = MessageHandler(filters.TEXT, handle_message)
# application.add_handler(message_handler)


os.

application.run_polling()