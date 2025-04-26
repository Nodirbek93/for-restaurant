# Menu Selection - Oddiy Menu Tanlash Dasturi

Bu kichik Python dasturi foydalanuvchiga menyudan ovqat tanlash imkonini beradi.

## Loyihaning vazifasi

- Foydalanuvchiga bir nechta ovqat variantlari ko'rsatiladi.
- Foydalanuvchi menyudan o‘z tanlovini kiritadi.
- Agar tanlangan ovqat menyuda mavjud bo‘lsa, dastur uni tasdiqlaydi va "Yoqimli ishtaha!" tilaydi.
- Agar menyuda bo‘lmasa, foydalanuvchiga xatolik xabari chiqadi.

## Ishlatish uchun

1. Dastur ishga tushiriladi.
2. Menyudan bir taom tanlanadi va kiritiladi.
3. Natija ekranda ko‘rsatiladi.

## Dastur kodi

```python
print("Assalomu alaykum! Bugungi menyudan tanlang:")

menu = ['osh', 'manti', 'shashlik', 'somsa', 'lagmon']

for food in menu:
    print(f"- {food.title()}")

choice = input("\nQaysi taomni tanlaysiz? ").lower()

if choice in menu:
    print(f"Siz {choice.title()}ni tanladingiz. Yoqimli ishtaha!")
else:
    print("Kechirasiz, bu taom menyuda yo'q.")
