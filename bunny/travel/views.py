from django.shortcuts import render
from . models import Destination


# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'MALDIVES'
    dest1.desc = 'BEST BEACH VIEW'
    dest1.img = '7.jpg'
    dest1.price = '2000'

    dest2 = Destination()
    dest2.name = 'HYDERABAD'
    dest2.desc = 'CITY THAT NEVER SLEEPS'
    dest2.img = '8.jpg'
    dest2.price = '1000'

    dest3 = Destination()
    dest3.name = 'Thailand'
    dest3.desc = 'Lathren Festival'
    dest3.img = '9.jpeg'
    dest3.price = '3000'

    dest4 = Destination()
    dest4.name = 'Norway'
    dest4.desc = 'Northern lights'
    dest4.img = '10.jpg'
    dest4.price = '4000'
    
    dest5= Destination()
    dest5.name = 'South Korea'
    dest5.desc = 'BTS Concert'
    dest5.img = '11.jpeg'
    dest5.price = '5000'

    dest6= Destination()
    dest6.name = 'Venice'
    dest6.desc = 'Full of Bridges'
    dest6.img = '12.jpg'
    dest6.price = '6000'

    

    dests = [dest1,dest2,dest3,dest4,dest5,dest6]
    return render ( request,'index.html', {'dests' : dests} )

