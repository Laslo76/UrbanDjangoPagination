from django.shortcuts import render
from task1.models import News
from django.core.paginator import Paginator


# Create your views here
def blog(request):
    blog_template = './task1/blog.html'
    records = News.objects.all()
    per_page = request.GET.get("per_page")
    if per_page is None:
        per_page = 5
    per_page = int(per_page)
    paginator = Paginator(records, per_page=per_page)
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    context = {'records': page_obj,
               'page_number': page_number,
               'per_page': per_page,
               'set_page': range(1, 6)}
    return render(request, blog_template, context=context)
