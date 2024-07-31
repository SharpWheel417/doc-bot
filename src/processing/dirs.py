import os

if not os.path.exists("static/document"):
  os.mkdir("static/document")

if not os.path.exists("static/pdf"):
  os.mkdir("static/pdf")

if not os.path.exists("static/html"):
  os.mkdir("static/html")

if not os.path.exists("static/html/compressed"):
  os.mkdir("static/html/compressed")

if not os.path.exists("static/js"):
  os.mkdir("static/js")
if not os.path.exists("static/js/compressed"):
  os.mkdir("static/js/compressed")

if not os.path.exists("static/css"):
  os.mkdir("static/css")
if not os.path.exists("static/css/compressed"):
  os.mkdir("static/css/compressed")
