from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category

def post_list(request):
    queryset = Post.objects.filter(status=Post.STATUS_PUBLISHED).select_related("author", "category")
    category_slug = request.GET.get("category")
    active_category = None
    if category_slug:
        active_category = get_object_or_404(Category, slug=category_slug)
        queryset = queryset.filter(category=active_category)
    paginator = Paginator(queryset, 9)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "blog/list.html", {
        "page_title": "Blog",
        "page_obj": page_obj,
        "categories": Category.objects.all(),
        "active_category": active_category,
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.STATUS_PUBLISHED)
    related = Post.objects.filter(status=Post.STATUS_PUBLISHED, category=post.category).exclude(pk=post.pk)[:3]
    return render(request, "blog/detail.html", {"page_title": post.title, "post": post, "related_posts": related})
