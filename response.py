# from datetime import datetime
import db as database


def inputText(input):
    print(input)
    try:
        return str(database.get_coin(input))
    except:
        return "العملة غير موجودة، تاكد من كتابة ا" \
               "لعملة بشكل صحيح"
    # if 'vol' in input:
    #     return "Vol is : " + "11111"
    #
    # if 'price' in input:
    #     return "price is : " + "10000"
    # if '😝' in input:
    #     return '🤪🤪🤪'
    # return str(datetime.now())
