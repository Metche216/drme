from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from pages.data import PROCEDURES


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['index', 'surgeries', 'diagnostic', 'about', 'testimonials', 'privacidad', 'terminos']

    def location(self, item):
        return reverse(item)


class ProcedureSitemap(Sitemap):
    priority = 0.9  # Higher than general pages — these are ad landing pages
    changefreq = 'monthly'

    def items(self):
        return list(PROCEDURES.keys())

    def location(self, slug):
        return reverse('procedure_landing', kwargs={'procedure_slug': slug})
