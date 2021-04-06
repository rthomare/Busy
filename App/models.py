from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator
from Sources.gif_helper import BusyGiphyClient

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    busy = models.BooleanField()
    busy_image = models.CharField(max_length=200)
    not_busy_image = models.CharField(max_length=200)

    # Constants in Model class
    GIPHY_SHUFFLE_SEARCH = 'GIPHY_SHUFFLE_SEARCH'
    GIPHY_RANDOM_SEARCH = 'GIPHY_RANDOM_SEARCH'
    GIPHY_TOP_SEARCH = 'GIPHY_TOP_SEARCH'
    RAW_URL = 'RAW_URL'
    GIF_SEARCH_TYPE_CHOICES = (
        (RAW_URL, 'URL'),
        (GIPHY_TOP_SEARCH, 'Giphy Top Search'),
        (GIPHY_RANDOM_SEARCH, 'Giphy Random Search'),
        (GIPHY_SHUFFLE_SEARCH, 'Giphy Shuffle Search'),
    )
    gif_search_type = models.CharField(
        max_length=100,
        choices=GIF_SEARCH_TYPE_CHOICES,
        default=RAW_URL,
    )

    def __giphy_image(self, term):
        value = None
        if (self.gif_search_type == self.GIPHY_TOP_SEARCH):
            value = BusyGiphyClient.get_giphy_top_search_image_url(term)
        elif (self.gif_search_type == self.GIPHY_RANDOM_SEARCH):
            value = BusyGiphyClient.get_giphy_random_image_url(term)
        elif (self.gif_search_type == self.GIPHY_SHUFFLE_SEARCH):
            value = BusyGiphyClient.get_giphy_shuffle_image_url(term)
        return value

    @property
    def busy_image_url(self):
        value = self.__giphy_image(self.busy_image)
        if (value is not None):
            return value
        return self.busy_image

    @property
    def not_busy_image_url(self):
        value = self.__giphy_image(self.not_busy_image)
        if (value is not None):
            return value
        return self.not_busy_image

    @property
    def image_url(self):
        if (self.busy):
            return self.busy_image_url
        else:
            return self.not_busy_image_url

