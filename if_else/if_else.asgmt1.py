sale_input = input("ยอดขาย (บาท): ")
sale_amount = float(sale_input)

if sale_amount > 10000:
    discount = sale_amount * 0.05
elif sale_amount > 5000:
    discount = sale_amount * 0.02
else:
    discount = 0

print("ส่วนลด =", discount, "฿")
net_sale = sale_amount - discount
print("รายได้หลังหักส่วนลด =", net_sale, "฿")

#VAT
if net_sale > 0:
    vat = net_sale * 0.07
    final_sale = net_sale - vat
    print(f"VAT (7%) = {vat:.2f} ฿")
    print("ยอดขายสุทธิหลังหัก VAT =", final_sale, "฿")
else:
    print("กรอกยอดขายให้ถูกต้อง")

#profit
cost = float(input("ราคาต้นทุน: "))
price = final_sale  

if price > cost:
    print("กำไร =", price - cost, "฿")
elif price < cost:
    print("ขาดทุน =", abs(price - cost), "฿")
else:
    print("เท่าทุน (Break even)")