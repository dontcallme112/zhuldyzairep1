from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, "./primary/index.html")

def news_page(request):
    return render(request, "./primary/news.html")

def news_detail_page(request):
    return render(request, "./primary/news-detail.html")
