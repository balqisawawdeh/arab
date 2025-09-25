from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Do something with the data, like send an email or save to DB
        messages.success(request, 'Thank you for contacting us!')
        return redirect('contact-us.html')

    return render(request, 'contact-us.html')

def about_us_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Do something with the data, like send an email or save to DB
        messages.success(request, 'Welcome To About Us!')
        return redirect('about-us')

    return render(request, 'about-us.html')

def company_history_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Do something with the data, like send an email or save to DB
        messages.success(request, 'company history!')
        return redirect('company-history')

    return render(request, 'company-history.html')

def services_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Do something with the data, like send an email or save to DB
        messages.success(request, 'services!')
        return redirect('services')

    return render(request, 'services.html')

def testimonials_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Do something with the data, like send an email or save to DB
        messages.success(request, 'testimonials!')
        return redirect('testimonials')

    return render(request, 'testimonials.html')

def request_quote_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Do something with the data, like send an email or save to DB
        messages.success(request, 'Thank you for contacting us!')
        return redirect('request-quote')

    return render(request, 'request-quote.html')

def teams_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Do something with the data, like send an email or save to DB
        messages.success(request, 'teams!')
        return redirect('teams')

    return render(request, 'teams.html')

def portfolio_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Do something with the data, like send an email or save to DB
        messages.success(request, 'portfolio!')
        return redirect('portfolio')

    return render(request, 'portfolio.html')

def faqs_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Do something with the data, like send an email or save to DB
        messages.success(request, 'faqs!')
        return redirect('faqs')

    return render(request, 'faqs.html')

def how_weather_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Do something with the data, like send an email or save to DB
        messages.success(request, 'how_weather_view!')
        return redirect('how_weather_view')

    return render(request, '/how-weather-can-impact-a-construction-project/index.html')

def how_choose_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Do something with the data, like send an email or save to DB
        messages.success(request, 'how_choose_view!')
        return redirect('how_choose_view')

    return render(request, '/how-to-choose-the-perfect-construction-company/index.html')

def healthcare_facility_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Do something with the data, like send an email or save to DB
        messages.success(request, 'healthcare_facility_view!')
        return redirect('healthcare_facility_view')

    return render(request, 'portfolio/healthcare-facility/index.html')

def Abattoir_Facility_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Do something with the data, like send an email or save to DB
        messages.success(request, 'Abattoir_Facility_view!')
        return redirect('Abattoir_Facility_view')

    return render(request, 'portfolio/Abattoir-Facility/index.html')

def Development_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Do something with the data, like send an email or save to DB
        messages.success(request, 'Development_view!')
        return redirect('Development_view')

    return render(request, 'portfolio/Development/index.html')

def Infrastructure_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Do something with the data, like send an email or save to DB
        messages.success(request, 'Infrastructure_view!')
        return redirect('Infrastructure_view')

    return render(request, 'portfolio/Infrastructure_view/index.html')