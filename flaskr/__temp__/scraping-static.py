from requests_html import HTMLSession

session = HTMLSession()
r = session.get(
    'https://huggingface.co/models')
articles = r.html.find('article header')

for idx, article in enumerate(articles):
    print(idx, article.text)
