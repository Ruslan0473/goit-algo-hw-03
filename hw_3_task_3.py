import re
raw_numbers = ["067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ","+380 44 123 4567",]

def normalize_phone(phone_number):
    p0=r"[\d\+]+"
    phone_number=''.join(re.findall(p0,phone_number))
    if len(phone_number)==10:
        phone_number='+38'+phone_number
    elif len(phone_number)==12:
        phone_number='+'+phone_number
    return phone_number


for phone_number in raw_numbers:
    print(normalize_phone(phone_number))