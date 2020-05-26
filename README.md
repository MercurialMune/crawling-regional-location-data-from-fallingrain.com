## crawling regional data from [here](http://fallingrain.com)
- plus a corresponding django [fixture](https://github.com/MercurialMune/crawling-regional-location-data-from-fallingrain.com/blob/master/location.json) for all locations
- can also be used for any country in the world
- just edit the country code in the urls

* the fixture assumes you have a django model in this format:
```python
from django.contrib.postgres.fields import ArrayField

class Location( models.Model ):
    county = models.CharField( max_length=100 )
    places = ArrayField( models.CharField( max_length=100 ), blank=True )

    def __str__(self):
        return self.county
```

* just run ```./manage.py loaddata location.json``` to populate your model
* running ```./location2.py``` will generate a json file called ```all_places.json``` if you need your data to be in a normal json format - for use with other languages/frameworks




