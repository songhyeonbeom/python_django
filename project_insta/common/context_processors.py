from .models import User, UserManager

def menu_links3(request) :
    links3 = User.objects.all()
    return dict(links3 = links3)


