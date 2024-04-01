from django.shortcuts import render, redirect
from fronpage.utils.common_functions import split_words
import csv
import os
import random


def submit_form(request):
    path_to_final_csv = os.getcwd() + '/fronpage/data/selection.csv'
    if request.method == 'POST':
        text_option = request.POST.get('text_option')
        zoomer_word, choice = split_words(text_option)

        with open(path_to_final_csv, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)  # Read all rows into a list

        for row in rows:
            if row[0] == zoomer_word:
                # Increment the value in the first index
                row[int(choice)] = str(int(row[int(choice)]) + 1)  # Increment the value
                final_list_display = row

        with open(path_to_final_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)

        # Process the form data as needed
        # Redirect to another page
            
        name_zoomer_word = final_list_display[0]
        final_list_display.pop(0)
        return render(request, 'thankyou.html', {'zoomer_word':name_zoomer_word, 'list': final_list_display})  # Redirects to /thank-you URL
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

    for x in range(len(options)):
        options[x] = str(x+1) + '. '+ options[x]

    return render(request, 'frontpage.html', {'zoomer_word': zoomer_word, 'options':options})

def thank_you(request):
    return render(request, 'thankyou.html')
