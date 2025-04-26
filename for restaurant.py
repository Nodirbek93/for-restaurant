

print("Assalomu alaykum! Bugungi menyudan tanlang:")

menu = ['osh', 'manti', 'shashlik', 'somsa', 'lagmon']

for food in menu:
    print(f"- {food.title()}")

choice = input("\nQaysi taomni tanlaysiz? ").lower()

if choice in menu:
    print(f"Siz {choice.title()}ni tanladingiz. Yoqimli ishtaha!")
else:
    print("Kechirasiz, bu taom menyuda yo'q.")
