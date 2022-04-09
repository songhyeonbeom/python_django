from .models import Photo, Album


def menu_links(request):
    customer = request.user.id
    print(request)
    links = Album.objects.filter(owner_id=customer)
    return dict(links = links)





def menu_links2(request) :
    allphoto = request.user.id
    links2 = Photo.objects.filter(owner_id=allphoto)
    return dict(links2 = links2)


