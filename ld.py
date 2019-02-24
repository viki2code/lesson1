l = [3,5,7,9,10.5]
print(l)
l.append('Python')
l_len = len(l)
print(l_len)
print(l[0])
print(l[l_len-1])
print(l[2:5])
l.remove('Python')
print (l)


city_info = {'city':'Москва', 'temperature':20}
print (city_info['city'])
city_info['temperature'] -= 5
print(city_info)
print(city_info.get('country'))
print(city_info.get('country','Россия'))
city_info['country'] ='Россия'
city_info['date'] ='27.05.2019'
print(city_info)