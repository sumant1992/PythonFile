import pandas as pd;

dict1 ={
	'name':['sumant','shubham','renuka','anju','shipra'],
     'mark':[20,10,15,11,52],
     'age':[15,16,25,45,30]
}

df = pd.DataFrame(dict1) 

print(df)