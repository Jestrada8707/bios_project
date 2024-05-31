from django.db import models

from wagtail.models import Page


class HomePage(Page):
    template = "index/index.html"
    max_count = 1
