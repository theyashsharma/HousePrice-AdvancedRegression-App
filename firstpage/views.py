from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import joblib

# Create your views here.
reloadModel = joblib.load('./Models/RFModelforSalePrice.pkl')

def index(request):
    context = {'a' : "Hello World"}
    return render(request,'index.html',context)


def predictPrice(request):
    print(request)
    if request.method == 'POST' :
        temp={}
        temp['LotArea'] = request.POST.get('LotArea')
        temp['GrLivArea'] = request.POST.get('GrLivArea')
        temp['1stFlrSF'] = request.POST.get('1stFlrSF')
        temp['TotalBsmtSF'] = request.POST.get('TotalBsmtSF')
        temp['BsmtFinSF1'] = request.POST.get('BsmtFinSF1')
        temp['GarageArea'] = request.POST.get('GarageArea')
        temp['WoodDeckSF'] = request.POST.get('WoodDeckSF')

    testData = pd.DataFrame({'x':temp}).transpose()
    priceval = reloadModel.predict(testData)[0]
    context = {'priceval' : priceval}
    return render(request, 'index.html', context)
