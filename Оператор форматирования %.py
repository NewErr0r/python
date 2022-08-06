template = """ <html>
<head>
    <title>%(title)s</title>
</head>
<body>
%(text)s
</body>
</html>"""

title = "Мой сайт"
body = "Много контента ... "

data = { "title": title,
          "text": body}

print(template % data)