from django.shortcuts import render, redirect

from regular_exam.web.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, EditProfileForm
from regular_exam.web.models import Profile, Car


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'core/index.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,

    }
    return render(request, 'profile/profile-create.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/profile-edit.html', context)


def details_profile(request):
    profile = get_profile()
    name = True
    cars = Car.objects.all()
    total_cars_price = sum(p.price for p in cars)
    if profile.name_generator is None:
        name = False
    context = {
        'profile': profile,
        'name': name,
        'cars': cars,
        'total_cars_price': total_cars_price,
    }
    return render(request, 'profile/profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteCarForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            Car.objects.all().delete()
            return redirect('index')

    return render(request, 'profile/profile-delete.html')


def catalogue(request):
    profile = get_profile()
    cars = Car.objects.all()
    context = {
        'profile': profile,
        'cars': cars,
    }
    return render(request, 'catalogue/catalogue.html', context)


def create_car(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'car/car-create.html', context)


def details_car(request, pk):
    profile = get_profile()
    cars = Car.objects.filter(pk=pk).get()

    context = {
        'profile': profile,
        'cars': cars,
    }
    return render(request, 'car/car-details.html', context)


def edit_car(request, pk):
    profile = get_profile()
    cars = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditCarForm(instance=cars)
    else:
        form = EditCarForm(request.POST, instance=cars)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'cars': cars,
        'form': form,
    }
    return render(request, 'car/car-edit.html', context)


def delete_car(request, pk):
    profile = get_profile()
    cars = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteCarForm(instance=cars)
    else:
        form = DeleteCarForm(request.POST, instance=cars)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'cars': cars,
        'form': form,
    }
    return render(request, 'car/car-delete.html', context)
