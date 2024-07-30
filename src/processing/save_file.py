async def save(file, new_file_path):
  try:
    # Получить файл из Telegram API
    file_obj = await file.get_file()
  except Exception as e:
    # await error_mess(str(e), update, context)
    print(str(e))
    return

    # Сохранить файл на диск с новым именем и путем
  with open(new_file_path, 'wb') as new_file:
    new_file_content = await file_obj.download_as_bytearray()
    new_file.write(new_file_content)