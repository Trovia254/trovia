from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLISHED = "published"
    STATUS_CHOICES = [(STATUS_DRAFT, "Draft"), (STATUS_PUBLISHED, "Published")]

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="published_at")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="blog_posts")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts")
    cover_image = models.ImageField(upload_to="blog/covers/", blank=True, null=True)
    excerpt = models.TextField(max_length=300, blank=True)
    body = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_DRAFT)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

    @property
    def read_time(self):
        return max(1, round(len(self.body.split()) / 200))

    def __str__(self):
        return self.title
