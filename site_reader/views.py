import urllib.request
from django.shortcuts import render
from site_reader.models import NewsEntry
from bs4 import BeautifulSoup


BASE_URL = 'https://news.ycombinator.com/'


def get_links_from_nav():
    response = urllib.request.urlopen(BASE_URL)
    soup = BeautifulSoup(response, "lxml")
    nav = soup.select('.pagetop a')
    href_list = []
    for item in nav:
        href_list.append(item['href'])

    return href_list


def iterate_pages(url, counter):
    context = {}
    news_list = []
    NewsEntry.objects.all().delete()
    for page in range(0, 100):
        if counter == 0:
            break
        counter -= 1
        print('Counter {}'.format(counter))
        print('PARSING PAGE #{}'.format(page))

        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response, "lxml")
        table = soup.find('table', class_='itemlist')
        next_page_button = soup.find('a', class_='morelink')

        rows = table.find_all('tr')
        result = []

        for row in rows:

            if row.has_attr('class') and row['class'] == ['athing']:
                cols = row.find_all('td')
                next_cols = row.next_sibling.find_all('td')
                site = cols[2].select_one('.sitestr')
                if site:
                    site = site.text

                news_entry = {
                    'number': cols[0].text.strip('.'),
                    'title': cols[2].a.text,
                    'author': next_cols[1].a.text,
                    'url': cols[2].a['href'],
                    'site': site,
                }
                q = NewsEntry.objects.create(title=str(news_entry['title']),
                               author=str(news_entry['author']),
                               url=str(news_entry['url']),
                               site=str(news_entry['site']))
                q.save()
                print(news_entry)
                result.append(news_entry)

        news_list.extend(result)
        if next_page_button is None:
            print('PARSE DONE')
            break
        url = BASE_URL + next_page_button['href']

    context['news_list'] = news_list

    return context['news_list'], counter




#
# class NewsListView(ListView):
#     model = NewsEntry
#
#     def get_queryset(self):
#         qs = super().get_queryset()