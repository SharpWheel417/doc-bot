import os

mass_dirs = ["static",
            "static/document",
            "static/pdf",
            "static/html",
            "static/html/compressed",
            "static/css",
            "static/css/compressed",
            "static/js",
            "static/js/compressed"]

for i in mass_dirs:
  if not os.path.exists(i):
    os.mkdir(i)