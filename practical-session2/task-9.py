salary ={'Abdeali': 20000,'Ali' :40000,'Kazim': 25000,'Katrina': 50000,'sarah':231312}
new_dict={k:v for (k,v) in salary.items() if v >= 25000 and v< 20000}
print(new_dict)
