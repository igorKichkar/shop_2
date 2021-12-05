from mainapp.models import *

a = Notebook.objects.get(pk=1)
print(a.price)