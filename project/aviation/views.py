from django.shortcuts import render
import pickle
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd 
# Create your views here.
def home(request):
    
    return render(request, 'home.html')


def result(request):
    example = [1.00000e+00,0.00000e+00,5.18670e+02,6.42440e+02, 1.58412e+03, 1.40642e+03,
 1.46200e+01, 2.16100e+01, 2.38803e+03, 9.04529e+03, 1.30000e+00, 4.72800e+01,
 2.38805e+03, 8.13290e+03, 8.39170e+00, 3.91000e+02]
    li_para = ['unit_number','setting_2', 'T2','T24','T30','T50','P2','P15','Nf',
 'Nc','epr','Ps30','NRf','NRc','BPR', 'htBleed' ]

    for ind, i in enumerate(li_para):
        value = request.GET.get(i)
        example[ind] = value
    example = pd.DataFrame(example)
    example = example.transpose()
    
    filename = 'train_classifier\model1.pkl'
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(example)
    dict = {'var': result}
    return render(request, 'result.html', dict)