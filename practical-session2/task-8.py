salary={'Saim':5000000,'Maaz':50,"Sohaib":10,"talha":400500}
new_dict={k for (k,v) in salary.items() if v>=40 and v<=60}
print(new_dict)