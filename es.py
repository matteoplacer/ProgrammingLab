class Model():

    def fit(self, data):
        pass
    
    def predict(self, data):
        pass

class IncrementModel(Model):

    def __str__(self):
        return 'IncrementModel'

    def compute_avg_increment(self, data):
        prev_item = None
        increments = 0

        for item in data:
            if prev_item is not None:
                increments += item - prev_item
            prev_item = item
        avg_increment = increments / (len(data)-1)
        
        return avg_increment

    def predict(self, predict_data):
        avg_increment = self.compute_avg_increment(predict_data)
        return predict_data[-1] + avg_increment


class FitIncrementModel(IncrementModel):

    def __str__(self):
        return 'FitIncrementModel'

    def fit(self, fit_data):
        self.global_avg_increment = self.compute_avg_increment(fit_data)

    def predict(self, predict_data):
        parent_prediction = super().predict(predict_data)
        parent_predict_increment = parent_prediction - predict_data[-1]
        prediction_increment = (self.global_avg_increment + parent_predict_increment) / 2
        prediction = predict_data[-1] + prediction_increment
        return prediction


test_fit_data = [8,19,31,41]
test_predict_data = [50,52,60]

# Test rapido su IncrementModel (non unit test in questo caso)
increment_model = IncrementModel()
prediction = increment_model.predict(test_predict_data) 
if not prediction == 65:
    raise Exception('IncrementModel sul dataset di test non mi torna 65 ma "{}"'.format(prediction))
else:
    print('IncrementModel test passed')

# Test rapido su FitIncrementModel (non unit test in questo caso)
fit_increment_model = FitIncrementModel()
fit_increment_model.fit(test_fit_data)
prediction = fit_increment_model.predict(test_predict_data)
if not prediction == 68:
    raise Exception('FitIncrementModel sul dataset di test non mi torna 68 ma "{}"'.format(prediction))
else:
    print('FitIncrementModel test passed')

# Linea vuota
print('')

shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]

eval_months = 12
cutoff_month = len(shampoo_sales) - eval_months

increment_model = IncrementModel()

fit_increment_model = FitIncrementModel()
fit_increment_model.fit(shampoo_sales[0:cutoff_month])

models = [increment_model, fit_increment_model]

for model in models:

    error = 0
    print('Evaluating model "{}"'.format(model))

    predictions = []
    for i in range(eval_months):
        predict_data = shampoo_sales[cutoff_month+i-3-1:cutoff_month+i-1]
        prediction = model.predict(predict_data)
        real = shampoo_sales[cutoff_month+i]
        print('"{}" (pred) vs "{}" (real)'.format(int(prediction), int(real)))

        predictions.append(prediction)

        error += abs(prediction - shampoo_sales[cutoff_month+i])
    
    error = error / eval_months

    print('Average error: "{}"\n'.format(error))


from matplotlib import  pyplot
pyplot.plot(shampoo_sales[0:cutoff_month] + predictions, color='tab:red')
pyplot.plot(shampoo_sales, color='tab:green')
pyplot.show()