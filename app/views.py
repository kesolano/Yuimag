from django.shortcuts import render, redirect
from .forms import  UserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from .models import Users_listt, Category, Photo


# Create your views here.

def home(request):
    return render(request, 'app/home.html')


def Users_Registration(request):
    data = {
        "form": UserForm()
    }

    if request.method == "POST":
        newForm = UserForm(data=request.POST)
        if newForm.is_valid():
            newForm.save()
            data["mensaje"] = "Registro exitoso"
        else:
            data["mensaje"] = "Hubo un problema, intentalo nuevamente"
            data["form"] = newForm
    return render(request, "app/Users_Registration.html", data)


def Userss(request):
    usuario = Users_listt.objects.all()
    return render(request, "app/Users.html", {"usuarios": usuario})


def Edit_User(request, username):
    usuario = Users_listt.objects.get(username=username)
    return render(request, "app/Edit_User.html", {"usuarios": usuario})


def Edit_list_user(request):
    username = request.POST["username"]
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    email = request.POST["email"]

    usuario = Users_listt.objects.get(username=username)
    usuario.fname = fname
    usuario.lname = lname
    usuario.email = email
    usuario.save()
    return redirect("/")


def Delete_User(request, username):
    usuario = Users_listt.objects.get(username=username)
    usuario.delete()
    return redirect("/")


def gallery(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.filter(category__user=user)
    else:
        photos = Photo.objects.filter(
            category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'photos': photos}
    return render(request, 'app/gallery.html', context)



def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'app/photo.html', {'photo': photo})



def addPhoto(request):
    
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
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


def Delete_Pic(request, pk):
    photo = Photo.objects.get(id=pk)
    photo.delete()
    return render(request, 'app/gallery.html')

