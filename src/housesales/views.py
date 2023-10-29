from django.shortcuts import render , HttpResponse
import joblib 

# Create your views here.



def index(request) : 
	return render(request,'index.html')

y_pred_globla  = 0 
def predict(request) : 
	data_user = []
	if request.method == 'POST' : 
		for element in request.POST :
			data_user.append(request.POST[element])

		tmp = data_user[1:]

		
		tmp_split = tmp[5].split('-')
		tmp = tmp[:-1]

		all_data = tmp + tmp_split

		all_data = [float(data) for data in all_data]

		print(all_data)

		## CALL MODEL 
		model = joblib.load('housesales/models/GradientBoostingRegressor_0_9843.joblib')

		## LAUNCH MODEL 

		y_pred = model.predict([all_data])
		y_pred_globla = y_pred[0]
		print(y_pred)
		
		content = {'y_pred' : y_pred_globla}

		return render(request, 'result.html', content)

		

	return render(request, 'predict.html')



def result(request): 
	content = {'y_pred' : y_pred_globla}
	return render(request, 'result.html', content)