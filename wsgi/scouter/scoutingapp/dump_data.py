import csv


def dump(qs, outfile_path):
    """
    Takes in a Django queryset and spits out a CSV file.

    Usage::

        >> from utils import dump2csv
        >> from dummy_app.models import *
        >> qs = DummyModel.objects.all()
        >> dump2csv.dump(qs, './data/dump.csv')

    Based on a snippet by zbyte64::
        http://www.djangosnippets.org/snippets/790/

    """
    model = qs.model
    writer = csv.writer(open(outfile_path, 'w'))

    headers = []
    for field in model._meta.fields:
        headers.append(field.verbose_name)
    writer.writerow(headers)

    headers = []
    for field in model._meta.fields:
        headers.append(field.name)

    for obj in qs:
        row = []
        for field in headers:
            val = getattr(obj, field)
            if callable(val):
                val = val()
            if type(val) == str:
                val = val.encode("utf-8")
            row.append(val)
        writer.writerow(row)
