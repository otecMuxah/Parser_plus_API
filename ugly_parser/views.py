from django.shortcuts import render
from site_reader.views import get_links_from_nav, iterate_pages ,BASE_URL





def index(request):
    counter = 100
    news_list = []
    pages_href_list = get_links_from_nav()
    for page in pages_href_list:
        temp, counter = iterate_pages(BASE_URL + '{}'.format(page), counter)
        news_list.extend(temp)
        if counter == 0:
            break
    return render(request, 'index.html', {'news_list': news_list})


