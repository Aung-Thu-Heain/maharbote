
import datetime

sun = ["puti", "binga", "a_htun", "yarza", "a_dipadi", "mayana", "thike"]  
mon = ["thike", "puti", "binga", "a_htun", "yarza", "a_dipadi", "mayana"]
tue = ["mayana", "thike", "puti", "binga", "a_htun", "yarza", "a_dipadi"]
wed = ["a_dipadi", "mayana", "thike", "puti", "binga", "a htun", "yarza"]
thu = ["yarza", "a dipadi", "mayana", "thike", "puti", "binga", "a_htun"]
fri = ["a_htun", "yarza", "a_dipadi", "mayana", "thike", "puti", "binga"]
sat = ["binga", "a_htun", "yarza", "a_dipadi", "mayana", "thike", "puti"]


def puti():
    print("မိတ်ေဆွ သင်သည် ပုတိဖွား ြဖစ်ပါသည်၊၊")


def binga():
    print("မိတ်ေဆွ သင်သည် ဘင်ဂဖွား ြဖစ်ပါသည်၊၊")


def a_htun():
    print("မိတ်ေဆွ သင်သည် အထွန်းဖွား ြဖစ်ပါသည်၊၊ ")
def yarza():
    print("မိတ်ေဆွ သင်သည် ရာဇဖွား ြဖစ်ပါသည်၊၊")
def a_dipadi():
    print("မိတ်ေဆွ သင်သည် အဓိပတိဖွား ြဖစ်ပါသည်၊၊")
def mayana():
    print("မိတ်ေဆွ သင်သည် မရဏဖွား ြဖစ်ပါသည်၊၊")
def thike():
    print("မိတ်ေဆွ သင်သည် သုိက်ဖွား ြဖစ်ပါသည်၊၊")


def forenglish():         #for english year         
    global year
    while True:
        try:
            date = int(input("ေမွးေန ့ (1,2,3,4,5,......) : "))     
            if 0 < date < 32:
                pass
            else:
                print("error-->ေမွးေန့မှာ 0 နှင့် 32 အြကားတွင်ရှိရပါမည်!!")
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]          #user ထည့်ေသာေမွးလကုိ တုိက်စစ်ြကည့်ရန်
            month = str(input("ေမွးလ(january,february,...) : ")).title() #့ြမန်မာနှစ်ြဖင့်တွက်ရာတွင် ေမွးလသိရန်မလုိေသာ်လည်း 
            if month in months:                                          #eng နှစ်ြဖင့်တွက်ရာတွင် april 17 ေကျာ်မေကျာ်သိရန် ေမွးလေမွးရက်ေတာင်းရ
                break                                                    #in english year,
            else:
                print("ေမွးလ မှားယွင်းေနပါသည်!")
        except:
            print("ေမွးေန ့မှာ 0 နှင့် 32 ြကားရှိဂဏန်းများသာ ြဖစ်ရပါမည်!")
    if month == "January":
        month = 1
    elif month == "February":
        month = 2
    elif month == "March":
        month = 3
    elif month == "April":
        month = 4
    elif month == "May":
        month = 5
    elif month == "June":
        month = 6
    elif month == "July":
        month = 7
    elif month == "August":
        month = 8
    elif month == "September":
        month = 9
    elif month == "October":
        month = 10
    elif month == "November":
        month = 11
    elif month == "December":
        month = 12

    inputdate = datetime.date(2000, month, date)
    maindate = datetime.date(2000, 4, 17)
    if inputdate < maindate:
        year -= 639

    else:
        year -= 638


while True:                                        #program အစ
    try:
        year = int(input("ေမွးသက္ကရာဇ်  : "))                        #မဟာဘုတ်တွက်ရန် user ေမွးနှစ်ေတာင်း
        if year >= 1500:                         #user မှ 1500 ေအာက်ကုိထည့်လျှင် ြမန်မာနှစ်ဟုသတ်မှတ် 1500 အထက်ထည့်လျှင် eng နှစ်ဟုသတ်မှတ်
            forenglish()
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",      
                "Saturday"]                          #user ထည့်ေသာေမွးနံ ကုိတုိက်စစ်ြကည့်ရန် 
        day = str(
            input("ေမွးနံ့ (sunday,monday,tuesday,wednesday,thursday,friday or saturday) : ")).title()     #user ေမွးနံ့ေတာင်း
        if day in days:
            break
        else:
            print("ေမွးနံ့မှားယွင်းသွားပါသည်။ြပန်ြကိုးစားပါ!")
    except:
        print("တစ်ခုုခု မှားယွင်းေနပါသည်။ြပန်ြကိုးစားပါ!")

if day == "Sunday":
    day = sun
elif day == "Monday":
    day = mon
elif day == "Tuesday":
    day = tue
elif day == "Wednesday":
    day = wed
elif day == "Thursday":
    day = thu
elif day == "Friday":
    day = fri
elif day == "Saturday":
    day = sat

module = year % 7
result = day[module]
if result == "puti":
    puti()
elif result == "binga":
    binga()
elif result == "a_htun":
    a_htun()
elif result == "yarza":
    yarza()
elif result == "a_dipadi":
    a_dipadi()
elif result == "mayana":
    mayana()
elif result == "thike":
    thike()
