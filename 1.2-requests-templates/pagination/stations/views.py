import pandas as pd
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import os
def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    data = pd.read_csv(r'E:\scripts(I_I)\First_project_django\1.2-requests-templates\data.csv')
        
    data_list = data.to_dict(orient='records')

    page_number = request.GET.get('page', 1)
    paginator = Paginator(data_list, 10)
    page_obj = paginator.get_page(page_number)
    context = {
        'bus_stations': page_obj,
        'page': page_obj,
    }
    return render(request, 'stations/index.html', context)

