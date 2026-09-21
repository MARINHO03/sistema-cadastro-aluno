medida=float(input('digite uma medida em metros:'))
dm=medida*10
cm=medida*100
mm=medida*1000
dam=medida/10
hm=medida/100
km=medida/1000
print('a medida {} corresponde a \n{}dm ,\n {}cm ,\n {}mm \n,{}dam \n,{}hm \n,{}km '.format(medida,dm,cm,mm,dam,hm,km))