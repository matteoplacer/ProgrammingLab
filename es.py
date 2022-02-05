class Model():
    def fit (self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict (self, data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    def predict(self, data):
        incremento = 0
        elem = 0
        for item in data:
            if(item >= 52):
                incremento = incremento+(item-elem)
            elem=item
        prediction = ((incremento/(len(data)-5)) + item)
        return prediction

class FitIncrementModel(IncrementModel):
    def fit(self,data):
        pass
    def predict(self,data):
        item_1=0
        i=0
        differenzialeTOT=0
        for item in data:
            if(i!=0):
                differenzialeTOT=differenzialeTOT+(item-item_1)
            item_1=item
            i=i+1
            if(i>len(data)-4):
                break    
        global_avg_increment=data[-1]+((differenzialeTOT/(len(data)-4))+super().predict(data)-data[-1])/2
        self.global_avg_increment=global_avg_increment
        return global_avg_increment

        
Modello=FitIncrementModel()
data=[8,19,31,41,50,52,60]
previsione=Modello.predict(data)
print("La previsione è: {}".format(previsione))