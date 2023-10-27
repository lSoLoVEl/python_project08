#OOP

class IotSAU :
    #data/property/field/attribute
    major = 'sau'
    name = ''

    #method (มันคือ funciton แต่เราไม่เรียบกฟังก์ชัน)
    def showHi(self) :
        print('Hi....')

    def introduceMySelf(self):
        print(f'My name is {self.name}')
        print(f'My major is {self.major}')

#---------------
#สร้าง object
obA=IotSAU()
obB=IotSAU()

#การใช้งาน data ของ objext คือ เอาค่ามันมาใช้ หรือเปลี่ยนคำให้มันใหม่
obA.major='Wow'
obA.major='ฟ้าร้อง'
obB.name='ฝนตกแล้ว'


#การใช้งาน method ของ objext คือ สั่งให้เมธอดของ object นั้นมาทำงาน
obA.introduceMySelf()
obB.introduceMySelf()