from django.shortcuts import render
from .forms import User_Register
from .models import Buyer, Game, News
from django.core.paginator import Paginator

def platform(request):
    return render(request, 'first_task/platform.html')

def shop(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'first_task/shop.html', context)

def basket(request):
    return render(request, 'first_task/basket.html')

def menu(request):
    return render(request, 'first_task/menu.html')

def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = User_Register(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            user_exist = Buyer.objects.filter(name=username).exists()

            if password == repeat_password and not user_exist and int(age) >= 18:
                Buyer.objects.create(name=username, balance=1500.0, age=age)
                return render(request, 'first_task/registration_page.html',
                              {'message': f'Приветствуем, {username}!', 'form': User_Register()})

            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif user_exist:
                info['error'] = 'Пользователь уже существует'

    else:
        form = User_Register()

    info['form'] = form
    return render(request, 'first_task/registration_page.html', info)

def view_news(request):
    news = News.objects.all().order_by('date')
    paginator = Paginator(news, 3)
    num_page = request.GET.get('page')
    page_obj = paginator.get_page(num_page)
    return render(request, 'news_temp/news.html', {'news': page_obj})

