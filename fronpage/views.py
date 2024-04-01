from django.shortcuts import render, redirect
import csv
import os
import random

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
    options = []
    with open(os.getcwd() + '/fronpage/data/options.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            options.append(row)

    ran_number = random.randint(0, len(options)-1)


    zoomer_word = options[ran_number][0]
    options[ran_number].pop(0)
    options = options[ran_number]

    return render(request, 'frontpage.html', {'zoomer_word': zoomer_word, 'options':options})

def thank_you(request):
    return render(request, 'thankyou.html')
