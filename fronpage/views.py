from django.shortcuts import render, redirect

def submit_form(request):
    if request.method == 'POST':
        text_option = request.POST.get('text_option')
        # Process the form data as needed
        # Redirect to another page
        return render(request, 'thankyou.html')  # Redirects to /thank-you URL
    else:
        return redirect('select_option')
# Create your views here.

def my_view(request):
    return render(request, 'frontpage.html')

def thank_you(request):
    return render(request, 'thankyou.html')
