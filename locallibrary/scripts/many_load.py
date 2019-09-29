import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, States, ISO, Region

def run():
    fhand = open('whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    Site.objects.all().delete()
    Category.objects.all().delete()
    States.objects.all().delete()
    ISO.objects.all().delete()
    Region.objects.all().delete()

    # Format
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python
    header = True
    for row in reader:
        print(row)
        if header is True:
            header = False
            continue
        c, created = Category.objects.get_or_create(name=row[7])
        st, created = States.objects.get_or_create(name=row[8])
        iso, created = ISO.objects.get_or_create(name=row[10])
        r, created = Region.objects.get_or_create(name=row[9])

        try:
            year = int(row[3])
        except:
            year = None
        try:
            longitude = float(row[4])
        except:
            longitude = None
        try:
            latitude = float(row[5])
        except:
            latitude = None
        try:
            area_hectares = float(row[6])
        except:
            area_hectares = None

        site = Site(name=row[0], year=year, longitude=longitude, latitude = latitude, area_hectares = area_hectares,
                    justification = row[2], description = row[1], category = c, states = st, iso = iso, region =r
                    )
        site.save()
