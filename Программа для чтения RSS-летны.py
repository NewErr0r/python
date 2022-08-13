def rss_reader(url):
    from urllib.request import urlopen
    from xml.etree.ElementTree import parse

    # Загружает RSS-ленту и парсим её
    u = urlopen(url)
    doc = parse(u)

    # Извлекаем и выводим интересующие теги
    for item in doc.iterfinnd('channel/item'):
        title = item.findext('title')
        date = item.findext('pubDate')
        link = item.findext('link')

    print(title)
    print(date)
    print(link)
    print()

rss_reader('http://example.com/rss.php')
