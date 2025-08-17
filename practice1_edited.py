
from collections import Counter

def normalize(text):
    """تبدیل حروف عربی به فارسی و حذف فاصله اضافی"""
    return text.replace('ي', 'ی').replace('ك', 'ک').strip()

def practice1(jomleh):
    yekta = [i for i in jomleh if jomleh.count(i) == 1]
    tartib_tekrar = dict(Counter(jomleh))
    return yekta, tartib_tekrar

while True:
    try:
        jomleh = input("\nJomle ra vared konid: ").split()
        yekta, tartib_tekrar = practice1(jomleh)

        # مرتب‌سازی: ابتدا تعداد نزولی، سپس ترتیب ورود اصلی
        list_moratab = sorted(
            tartib_tekrar.items(),
            key=lambda x: (-x[1], [i for i, w in enumerate(jomleh) if w == x[0]][0])
        )

        print(f"Kalamat yekta = {yekta}")
        print(f"Tartib tekrar kalamat = {list_moratab}")

        valid_answers = ["بلی", "خیر"]
        while True:
            payan = normalize(input("آیا ادامه میدهید؟ بلی/خیر: "))
            if payan in valid_answers:
                break
            else:
                print("لطفاً فقط 'بلی' یا 'خیر' وارد کنید.")

        if payan == "بلی":
            continue
        else:
            break

    except Exception as e:
        print(f"خطا رخ داد: {e}")
