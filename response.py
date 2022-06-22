from datetime import datetime

# from datetime import datetime

import dynmic_db as db

active_users = {}
last_clear_time = 999999999999


def inputText(input, id):
    global last_clear_time
    try:
        if int(datetime.utcnow().timestamp()) - last_clear_time > (60 * 30):
            active_users.clear()
            last_clear_time = int(datetime.utcnow().timestamp())
        if active_users.get(id) is None:
            active_users[id] = int(datetime.utcnow().timestamp())

            return str(db.get_coin_info(input.upper()))
        else:
            if int(datetime.utcnow().timestamp()) - active_users.get(id) > 10:
                active_users[id] = int(datetime.utcnow().timestamp())
                print(int(datetime.utcnow().timestamp()))
                return str(db.get_coin_info(input.upper()))
            else:
                return "انتظر قليلا قبل ارسال رسالة اخرى  ،حاول بعد ({}) ثانية".format(
                    (10) - (int(datetime.utcnow().timestamp()) - active_users.get(id)))
    except Exception as e:
        print(e)
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



