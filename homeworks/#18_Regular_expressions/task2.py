import re
import requests

if __name__ == "__main__":
    link = "http://socrates.vsau.org/wiki/index.php/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B0%D0%B4%D1%80%D0%B5%D1%81_%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%B8%D1%85_%D0%BF%D0%BE%D1%88%D1%82%D0%BE%D0%B2%D0%B8%D1%85_%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8C_%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%BD%D0%B8%D1%85_%D0%BF%D1%96%D0%B4%D1%80%D0%BE%D0%B7%D0%B4%D1%96%D0%BB%D1%96%D0%B2_%D1%83%D0%BD%D1%96%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D1%83"
    data = requests.get(link)

    paragraphs = re.finditer(r'<p>(?P<name>[\w\s\u0430,.\-\"]+)\n?<b>(?P<email>[a-zA-z0-9._@]+)', data.text)
    result1 = list((re.sub(r'\s*$', '', match.group('name')), match.group('email')) for match in paragraphs)
    print(f'Result #1 = ', result1)

    result2 = {}
    titles = re.finditer(
        r'\d{1,2}\.\s(?P<title>[\w\s\u0430,.\-\"]+)\<\/span><\/h2>\s*(<p>[\w\s\u0430,.\-\"]+<b>[a-zA-Z0-9_@.]+<\/b>\s?\n?(<\/p>)?)*',
        data.text)
    for title in titles:
        paragraphs = re.finditer(r'<p>(?P<name>[\w\s\u0430,.\-\"]+)\n?<b>(?P<email>[a-zA-z0-9._@]+)', title.group(0))
        result2.update({(re.sub(r'\s*$', '', title.group('title'))):
                            list((re.sub(r'\s*$', '', match.group('name')), match.group('email')) for match in paragraphs)})
    print(f'\nResult #2 = ', result2)
