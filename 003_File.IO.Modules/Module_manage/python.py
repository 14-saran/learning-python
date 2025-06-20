# import ชื่อmodule
# ชื่อmodule.ชื่อfmodule
import area_test

circle_area = area_test.circle_area(10)
print("พื้นที่วงกลม", circle_area)

triangle_area = area_test.triangle_area(10,15)
print("พื้นที่สามเหลี่ยม",triangle_area)

rectang_area = area_test.rectang_area(10,15)
print("พื้นที่สี่เหลี่ยม",rectang_area)


print("---------------------------------------")

#เลือกเฉพาะfที่ต้องการ
# from ชื่อmodule import ชื่อfunction

from area_test import circle_area,triangle_area

c_area = circle_area(10)
print("พื้นที่วงกลม",c_area)

t_area = triangle_area(10,15)
print("พื้นที่สามเหลี่ยม",t_area)

r_area = rectang_area(10,15)
print("พื้นที่สี่เหลี่ยม",r_area)