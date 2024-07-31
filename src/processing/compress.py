"""
Сжимает файл html и меняет пути до файлов чтобы потом строку закинуть на железку
"""

"""
pip install beautifulsoup4
pip install htmlmin
pip install jsmin
pip install cssmin
"""
from bs4 import BeautifulSoup
import htmlmin
import jsmin
import cssmin
import os


'''
Сжимает html файл и зменяет пути
'''
def compress_and_update_paths(html_content):
    # Сжатие HTML-кода
    minified_html = htmlmin.minify(html_content, remove_empty_space=True, remove_all_empty_space=True)

    # Парсинг HTML с помощью BeautifulSoup
    soup = BeautifulSoup(minified_html, 'html.parser')

    # Обновление путей к ресурсам в теге script
    # Найдем все теги 'script' с атрибутом 'src'
    scripts = soup.find_all('script', {'src': True})

    if len(scripts) >= 2:
        for script in scripts[:2]:
            script.extract()

    for tag in soup.find_all('script'):
        if 'src' in tag.attrs:
            tag['src'] = "/script.js"

    # Обновление путей к ресурсам в теге link с rel="stylesheet"
    for tag in soup.find_all('link', rel='stylesheet'):
        if 'href' in tag.attrs:
            tag['href'] = "/style.css"

    # Возвращаем сжатый и обновленный HTML
    return str(soup)

def process_html_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    updated_html = compress_and_update_paths(html_content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(updated_html)


def compress_js_files(source_folder: str, output_file: str):
  '''
  Сжимает js файлы из папки и обьединяет их все в один
  '''
  js_files = [os.path.join(source_folder, f) for f in os.listdir(source_folder) if f.endswith('.js')]

  with open(output_file, 'w', encoding='utf-8') as outfile:
      for js_file in js_files:
          # js = js_file.replace("\\", "/")
          with open(js_file, 'r', encoding='utf-8') as infile:
              minified_js = jsmin.jsmin(infile.read())
              outfile.write(minified_js)


def compress_css_files(source_folder: str, output_file: str):
    '''
    Сжимает css файлы из папки и объединяет их все в один
    '''
    css_files = [os.path.join(source_folder, f) for f in os.listdir(source_folder) if f.endswith('.css')]

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for css_file in css_files:
            with open(css_file, 'r', encoding='utf-8') as infile:
                minified_css = cssmin.cssmin(infile.read())
                outfile.write(minified_css)
