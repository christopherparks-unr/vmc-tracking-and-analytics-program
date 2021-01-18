from django.shortcuts import render
from . import scanner_parsing
from . import parser
from django.http import HttpResponse
import csv

import sqlite3

# Create your views here.

def parse(request):
    if request.method == 'POST' and request.FILES['datafile']:
    
        conn = sqlite3.connect('vmc_tap.db');
    
        data_file = request.FILES['datafile'].read().decode('utf-8').splitlines()
        data,tags,staff = parser.parse_report(data_file)
        return_string = ''
        total_duration = 0
        for visit in data:
            return_string += str(visit) + '<br>'
            #Insert data into database
            conn.execute(visit.get_insert_statement())
        conn.commit();
        return_string += 'Number of Visits: ' + str(len(data)) + '.<br>'
        
        #return_string += 'This data has been inserted into the database.<br>'
        
        return HttpResponse(return_string)
    else:
        return HttpResponse("ERROR, please go to the import page and upload a file.")

