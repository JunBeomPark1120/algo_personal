x = 20  # 20% 농도 소금물의 농도

y = 100 # 20% 농도의 100g 물

w = 200 # 아무것도 모르는 농도의 200g의 물

z = x / (y + w) * 100 #구해야 할 농도

print(f'혼합된 소금물의 농도: {z:.2f}%')