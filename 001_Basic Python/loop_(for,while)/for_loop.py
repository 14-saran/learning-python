#for loop = execute a block of code a fixed number od time.
#   you can interate over a range, string, sequence, etc.

for x in (range(1,6,2)):
    print(x)
print("ONLY MONDAY")

print('-----------------------------------------')

credit_card = "1-451-469"
for a in credit_card:
    print(a)

print('-----------------------------------------')
for b in range(1,8):
    if b == 5 :
        continue #(ข้ามเลข5ไป)
    else:
        print(b)

print('-----------------------------------------')
for b in range(1,8):
    if b == 5 :
        break #(หยุดก่อนถึงเลข5)
    else:
        print(b)