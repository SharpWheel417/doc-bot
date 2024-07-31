from cgitb import text
import os
import telegram
from telegram import Update, Bot
from telegram.ext import CallbackContext
import docx2pdf
import subprocess

from ..processing.compress import process_html_file, compress_js_files, compress_css_files

from ..processing.save_file import save

from ..view.send import sendmess, senddoc


async def handle_html(update: Update, context: CallbackContext):
    '''
    Сжимает html
    '''

    file = update.message.document
    file_name = file.file_name
    file_name = file_name.split('.')[0]

    file_path = 'static/html/'+str(file_name)+'.html'
    compres_file_path = 'static/html/compressed/'+str(file_name)+'_compress.html'

    ## Сохраняем файл в папке
    await save(file, file_path)

    ## Обрабатываем файл
    process_html_file(file_path, compres_file_path)


    # Отправляем PDF обратно пользователю
    with open(compres_file_path, 'rb') as f:
        await sendmess("Сжатие прошло успешно", update, context)


async def handle_css(update: Update, context: CallbackContext):
    '''
    Сжимает css
    '''
    file = update.message.document
    file_name = file.file_name
    file_name = file_name.split('.')[0]

    file_path = 'static/css/'+str(file_name)+'.css'
    compres_file_path = 'static/css/compressed/'+str(file_name)+'_compress.css'

    ## Сохраняем файл в папке
    await save(file, file_path)

    ## Обрабатываем файл
    process_html_file(file_path, compres_file_path)


    # Отправляем PDF обратно пользователю
    with open(compres_file_path, 'rb') as f:
        await senddoc(f=f, text="Сжатие прошло успешно", update=update, context=context)




async def handle_js(update: Update, context: CallbackContext):
    '''
    Сжимает js
    '''
    # Обработка одиночного файла
    file = update.message.document
    file_name = file.file_name
    file_name = file_name.split('.')[0]
    file_path = 'static/js/'+str(file_name)+'.js'
    compres_file_path = 'static/js/compressed/'+str(file_name)+'_compress.js'
    ## Сохраняем файл в папке
    await save(file, file_path)
    # Добавьте сюда логику для обработки файла, например, сжатие
    process_html_file(file_path, compres_file_path)
    # Отправляем PDF обратно пользователю
    with open(compres_file_path, 'rb') as f:
            await senddoc(f=f, text='Сжатый файл', update=update, context=context)








async def handle_document(update: Update, context: CallbackContext):
    '''
        Обрабатывает DocX, dox
    '''

    sendmess('Файл пришел', update, context)

    # Получить файл из обновления
    file = update.message.document

    # Получить имя файла
    file_name = file.file_name
    file_name = file_name.replace('.docx', '')


    new_file_path = os.path.join("static/document", str(file_name)+ '.docx')
    pdf_path = os.path.join("static/pdf/", str(file_name)+'.pdf')

    try:
        # Получить файл из Telegram API
        file_obj = await file.get_file()
    except Exception as e:
        # await error_mess(str(e), update, context)s
        sendmess(e, context=context, update=update)
        return

    # Сохранить файл на диск с новым именем и путем
    with open(new_file_path, 'wb') as new_file:
        new_file_content = await file_obj.download_as_bytearray()
        new_file.write(new_file_content)

    await sendmess("Файл сохранен, начинается обработка", update, context)

    try:
        command = ['pandoc', new_file_path, '-o', pdf_path, '--pdf-engine=wkhtmltopdf']
        subprocess.run(command, check=True)

        # # Конвертируем docx в PDF
        # docx2pdf.convert("static/document/" + str(file_name)+'.docx', "static/pdf/"+ str(file_name)+'.pdf')
    except Exception as e:
        await sendmess(e, update, context)

    await sendmess("Обработка завершена, ожидайте файл", update, context)

    # Отправляем PDF обратно пользователю
    with open('static/pdf/'+str(file_name)+'.pdf', 'rb') as f:
        await senddoc(f=f, text="Сжатый файл:", update=update, context=context)