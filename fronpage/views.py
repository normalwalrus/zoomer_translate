from django.shortcuts import render, redirect
from fronpage.utils.common_functions import split_words
import csv
import os
import random


def submit_form(request):
    path_to_final_csv = os.getcwd() + '/fronpage/data/selection.csv'
    path_to_options_csv = os.getcwd() + '/fronpage/data/options.csv'
    path_to_checking_csv = os.getcwd() + '/fronpage/data/checking.csv'
    path_to_filtered_csv = os.getcwd() + '/fronpage/data/filtered_selections.csv'
    path_to_checkselection_csv = os.getcwd() + '/fronpage/data/checking_selections.csv'
    if request.method == 'POST':
        text_option = request.POST.get('text_option')
        zoomer_word, choice = split_words(text_option)
        choice = int(choice)

        check_option = request.POST.get('check_option')
        check_word, check_choice = split_words(check_option)
        check_choice = int(check_choice)

        with open(path_to_checkselection_csv, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            row_checksel = list(reader)

        with open(path_to_checking_csv, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows_q1 = list(reader)

        with open(path_to_filtered_csv, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows_filtered = list(reader)

        for index, row in enumerate(rows_q1):
            if row[0] == check_word:
                row.pop(0)
                row_checksel[index][int(check_choice)] = str(int(row_checksel[index][int(check_choice)]) + 1)
                check_list_display = rows_filtered[index]
                if int(row[3])+1 == check_choice:
                    rows_filtered[index][int(check_choice)] = str(int(rows_filtered[index][int(check_choice)]) + 1)
                    check_list_display = rows_filtered[1:]
                checked_options = row[:3]

        with open(path_to_filtered_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows_filtered)

        with open(path_to_checkselection_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(row_checksel)

        with open(path_to_final_csv, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)  # Read all rows into a list

        for row in rows:
            if row[0] == zoomer_word:
                # Increment the value in the first index
                row[int(choice)] = str(int(row[int(choice)]) + 1)  # Increment the value
                final_list_display = row

        with open(path_to_options_csv, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows_options = list(reader)  # Read all rows into a list

        for row in rows_options:
            if row[0] == zoomer_word:
                # Increment the value in the first index
                row.pop(0)
                options = row[:3]

        with open(path_to_final_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)

        # Process the form data as needed
        # Redirect to another page
            
        name_zoomer_word = final_list_display[0]
        final_list_display.pop(0)
        return render(request, 'thankq.html', {'zoomer_word':name_zoomer_word, 'list': final_list_display, "choice":choice, 'options':options, 'check_word':check_word, 'check_list':check_list_display, 'check_choice':check_choice, 'checked_options':checked_options})  # Redirects to /thank-you URL
    else:
        return redirect('select_option')
# Create your views here.

def my_view(request):
    options, options_checking = [], []

    #for displaying q1(checking)
    with open(os.getcwd() + '/fronpage/data/checking.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            options_checking.append(row[:4])
    
    ran_number = random.randint(0, len(options_checking)-1)

    check_word = options_checking[ran_number][0]
    options_checking[ran_number].pop(0)
    options_checking = options_checking[ran_number]

    for x in range(len(options_checking)):
        options_checking[x] = str(x+1) + '. '+ options_checking[x]

    with open(os.getcwd() + '/fronpage/data/options.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            options.append(row[:4])

    ran_number = random.randint(0, len(options)-1)

    zoomer_word = options[ran_number][0]
    options[ran_number].pop(0)
    options = options[ran_number]

    for x in range(len(options)):
        options[x] = str(x+1) + '. '+ options[x]

    return render(request, 'frontpage.html', {'zoomer_word': zoomer_word, 'options':options, 'check_word':check_word, 'options_checking':options_checking})

def thank_you(request):
    return render(request, 'thankyou.html')
