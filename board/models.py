from django.db import models


class Post(models.Model):
    TAGS = [
        (0, '소분'),
        (1, '나눔'),
        (2, '완료'),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    image1 = models.ImageField(upload_to="posts/img")
    image2 = models.ImageField(upload_to="posts/img", blank=True, null=True)
    image3 = models.ImageField(upload_to="posts/img", blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.PositiveSmallIntegerField(choices=TAGS)
    price = models.PositiveIntegerField(default=0)
    user_key = models.PositiveIntegerField()
