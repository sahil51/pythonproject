# Google translator
from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES,Translator

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'et': 'estonian',
    'fi': 'finnish',
    'fr': 'french',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'he': 'hebrew',
    'hi': 'hindi',
    'hu': 'hungarian',
    'is': 'icelandic',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'kn': 'kannada',
    'ko': 'korean',
    'ku': 'kurdish',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'mk': 'macedonian',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'oriya',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sr': 'serbian',
    'st': 'sesotho',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'es': 'spanish',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu'
}

root = Tk()
root.geometry("1500x900")
root["bg"]="light blue"
root.title("Language Translators")

# to add functionality in  our translator:    
def translatooor():
    translate = Translator()
    translate_text = translate.translate(text=input_box.get(1.0,END), src=input_lang.get(), dest=output_lang.get())
    output_box.delete(1.0,END)
    output_box.insert(END, translate_text.text)

# heading of project in window
lbl1 = Label(root, text="Language Translator",font="arial 30 bold",borderwidth=4,relief="sunken",bg="light yellow")
lbl1.pack(pady=10)
#  user Input language block:
frm=Frame(root,width=500,height=550,bg="pink",bd=30,highlightbackground="black",highlightthickness=3)
frm.place(x=200,y=90)
input_label=Label(root, text="Input language",font="arial 15 bold" ,bd=10 ,borderwidth=2,relief="solid",height=2,bg="wheat")
input_label.place(x=230,y=130)
languages= list(LANGUAGES.values())
input_lang=ttk.Combobox(root,values=languages)
input_lang.set("select languages")
input_lang.place(x=430,y=135,height=35)
# user output Language block:
frm=Frame(root,width=500,height=550,bg="pink",bd=30,highlightbackground="black",highlightthickness=3)
frm.place(x=870,y=90)
output_label=Label(root, text="Output language",font="arial 15 bold", bd=10,borderwidth=2,relief="solid",height=2,bg="wheat")
output_label.place(x=900,y=130)
output_lang=ttk.Combobox(root,values=languages)
output_lang.set("select languages")
output_lang.place(x=1150,y=135,height=35)
input_box=Text(root,  width=43,height=15,background="light yellow",borderwidth=4,relief="sunken")
input_box.place(x=256,y=235)
output_box=Text(root, width=44,height=15,background="light yellow",borderwidth=4,relief="sunken")
output_box.place(x=930,y=235)
# Translate button
btns=Button(root,text="Translate",font="arial 15 bold",bd=10,bg="light green",command=translatooor)
btns.place(x=680,y=670,height=55,width=220)
root.mainloop()
