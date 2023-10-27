#***Dictionary คือข็อมูลหลายข้อมูล ที่เป็น key:value แก้ไขได้ด้วย ไม่มีลำดับ ซ้ำได้
# key เป้นString/Integer ก็ได้ ส่วน value เป็นอัหนังก็ได้ (number,string,boolean,list,tuple,set,dictionary)
my_dict1={'name':'mod','age':30,555:999,'flag':True,'wow':[10,20,30]}

my_dict2={ 'data1':[10,30,40],
          'data2':(2,5,6),
          'data3':{45,3,4},
          'data4':{'x':111,
                   'y':222
                   }
                   }

#การเข้าถึงข้อมูลใกข้อมูลหนึ่ง
print(my_dict1['name'])
print(my_dict1[555])
my_dict1['age']=50
print(my_dict1)
#อยากแสดงผล20 ออกมา
print(my_dict1['wow'][1])
#อยากได้  222
print(my_dict2['data4']['y'])
print(my_dict2)
my_dict2['data5']=888
print(my_dict2)
#การเข้าถึงทุกข้อมูล
for xx in my_dict1 :
    print(xx)

print('-----------------------')
for xx in my_dict1.keys( ) :
    print(xx)

print('-----------------------')
for xx in my_dict1.values( ) :
    print(xx)

print('-----------------------')
for xx,yy in my_dict1.item( ) :
    print(xx, '-', yy)

#Dictionary method
my_dict1.popitem()
my_dict1.popitem()
my_dict1.popitem()
print(my_dict1)
my_dict2.pop('data3')
print(my_dict2)
