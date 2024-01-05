from . models import *
from . views import *

def count(request):
    item_count=0;
    if 'admin'in request.path:
        return {}
    else:
        try:
            ct=cartlist.objects.filter(cart_id=c_id(request))
            ct_i=items.objects.all().filter(cart=ct[:1])
            for c in ct_i:
                item_count+=c.quantity

        except cartlist.DoesNotExist:
                item_count=0
        return dict(i_count=item_count)