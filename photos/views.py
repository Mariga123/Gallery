from django.shortcuts import render
from .models import Image,Location
# Create your views here.

def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'photos/index.html', {'images': images[::-1], 'locations': locations})


def location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'photos/find.html', {'location_images': images})


def search(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'photos/search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'photos/search.html', {"message": message})