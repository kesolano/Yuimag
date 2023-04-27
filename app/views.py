from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Users_listt, Category, Photo



# Create your views here.
# Input parameter: a request object that contains information about the incoming HTTP request.
# Output: renders a HTML template named home.html using the render() function provided by the Django framework.

def home(request):
    return render(request, 'app/home.html')

# Input parameter: a request object that contains information about the incoming HTTP request.
# Output: renders a HTML template named Users_Registration.html using the render() function provided by the Django framework, along with a form object that contains a UserForm instance.


def Users_Registration(request):
    data = {
        "form": UserForm()
    }

    if request.method == "POST":
        newForm = UserForm(data=request.POST)
        if newForm.is_valid():
            newForm.save()
            data["mensaje"] = "Registro exitoso"
            return redirect('Users')
        else:
            data["mensaje"] = "Hubo un problema, intentalo nuevamente"
            data["form"] = newForm
    return render(request, "app/Users_Registration.html", data)


# Input parameter: a request object that contains information about the incoming HTTP request.
# Output: renders a HTML template named Users.html using the render() function provided by the Django framework, along with a usuarios object that contains all Users_listt instances.
# Functionality: retrieves all Users_listt instances from the database and displays them in the HTML template.

def Userss(request):
    usuario = Users_listt.objects.all()
    return render(request, "app/Users.html", {"usuarios": usuario})


# Input parameters: a request object that contains information about the incoming HTTP request, and a username string that represents the username of the user to be edited.
# Output: renders a HTML template named Edit_User.html using the render() function provided by the Django framework, along with a usuarios object that contains the Users_listt instance with the specified username.
# Functionality: retrieves the Users_listt instance with the specified username from the database and displays it in the HTML template.

def Edit_User(request, id):
    usuario = Users_listt.objects.get(pk=id)
    return render(request, "app/Edit_User.html", {"usuarios": usuario})


# Input parameter: a request object that contains information about the incoming HTTP request.
# Output: redirects the user to the home page of the web application.
# Functionality: retrieves the form data submitted with the request and updates the corresponding Users_listt instance in the database.

def Edit_list_user(request, id):
    username = request.POST["username"]
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    email = request.POST["email"]

    usuario = Users_listt.objects.get(pk=id)
    usuario.username = username
    usuario.fname = fname
    usuario.lname = lname
    usuario.email = email
    usuario.save()
    return redirect('Users')


# Input parameters: a request object that contains information about the incoming HTTP request, and a username string that represents the username of the user to be deleted.
# Output: redirects the user to the home page of the web application.
# Functionality: retrieves the Users_listt instance with the specified username from the database and deletes it.

def Delete_User(request, id):

    usuario = Users_listt.objects.get(pk=id)
    usuario.delete()
    return redirect('Users')


def gallery(request):

    category = request.GET.get("category")
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name__contains=category)



    categories = Category.objects.all()
    

    context = {"categories": categories, "photos": photos}
    return render(request, 'app/gallery.html', context)


# Input parameter: a request object that contains information about the incoming HTTP request.
# Output: renders a HTML template named gallery.html using the render() function provided by the Django framework, along with a categories object that contains all Category instances and a photos object that contains all Photo instances.
# Functionality: retrieves all Category instances and Photo instances from the database based on the user and category parameters in the request, and displays them in the HTML template.

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'app/photo.html', {'photo': photo})


# Input parameters: a request object that contains information about the incoming HTTP request, and a pk integer that represents the primary key of the photo to be viewed.
# Output: renders a HTML template named photo.html using the render() function provided by the Django framework, along with a photo object that contains the Photo instance with the specified primary key.
# Functionality: retrieves the Photo

def addPhoto(request):

    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'app/add.html', context)


def Delete_Category(request, id):
    category = Category.objects.get(pk=id) 
    category.delete()
    return redirect('gallery')


def Delete_Image(request, id):

    usuario = Photo.objects.get(pk=id)
    usuario.delete()
    return redirect('gallery')

