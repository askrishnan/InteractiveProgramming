import tkinter
from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
import urllib
import random

dictCountries = {'Afghanistan': 'Afghanistan', 'Albania': 'Albania',
                 'Algeria': 'Algeria', 'Andorra': 'Andorra', 'Angola': 'Angola',
                 'Antigua and Barbuda': 'Antigua_and_Barbuda',
                 'Argentina': 'Argentina', 'Armenia': 'Armenia',
                 'Australia': 'Australia', 'Austria': 'Austria',
                 'Azerbaijan': 'Azerbaijan',
                 'The Bahamas': 'The_Bahamas', 'Bahrain': 'Bahrain',
                 'Bangladesh': 'Bangladesh', 'Barbados': 'Barbados',
                 'Belarus': 'Belarus', 'Belgium': 'Belgium', 'Belize': 'Belize',
                 'Benin': 'Benin', 'Bhutan': 'Bhutan', 'Bolivia': 'Bolivia',
                 'Bosnia and Herzegovina': 'Bosnia_and_Herzegovina',
                 'Botswana': 'Botswana', 'Brazil': 'Brazil', 'Brunei': 'Brunei',
                 'Bulgaria': 'Bulgaria', 'Burkina Faso': 'Burkina_Faso',
                 'Burundi': 'Burundi',
                 'Cambodia': 'Cambodia', 'Cameroon': 'Cameroon',
                 'Canada': 'Canada',
                 'Central African Republic': 'Central_African_Republic',
                 'Chad': 'Chad', 'Chile': 'Chile', 'China': 'China',
                 'Colombia': 'Colombia', 'Comoros':'Comoros',
                 'Democratic Republic of the Congo': 'Democratic_Republic_of_the_Congo',
                 'Republic of the Congo': 'Republic_of_the_Congo',
                 'Costa Rica': 'Costa_Rica', 'Croatia': 'Croatia',
                 'Cuba': 'Cuba', 'Cyprus': 'Cyprus',
                 'Czech Republic': 'Czech_Republic', 'Denmark': 'Denmark',
                 'Djibouti': 'Djibouti', 'Dominica': 'Dominica',
                 'Dominican Republic': 'Dominican_Republic',
                 'East Timor': 'East_Timor', 'Ecuador': 'Ecuador',
                 'Egypt': 'Egypt', 'El Salvador': 'El_Salvador',
                 'Equatorial Guinea': 'Equatorial_Guinea',
                 'Eritrea': 'Eritrea', 'Estonia': 'Estonia', 'Ethiopia': 'Ethiopia',
                 'Fiji': 'Fiji', 'Finland': 'Finland', 'France': 'France',
                 'Gabon': 'Gabon', 'Gambia': 'The_Gambia', 'Georgia': 'Georgia',
                 'Germany': 'Germany', 'Ghana': 'Ghana', 'Greece': 'Greece',
                 'Grenada': 'Grenada', 'Guatemala': 'Guatemala',
                 'Guinea': 'Guinea', 'Guinea-Bissau': 'Guinea-Bissau',
                 'Guyana': 'Guyana', 'Haiti': 'Haiti',
                 'Honduras': 'Honduras', 'Hungary': 'Hungary',
                 'Iceland': 'Iceland', 'India': 'India',
                 'Indonesia': 'Indonesia', 'Iran': 'Iran', 'Iraq': 'Iraq',
                 'Ireland': 'Ireland', 'Israel': 'Israel', 'Italy': 'Italy',
                 'Ivory Coast': 'Ivory_Coast', 'Jamaica': 'Jamaica',
                 'Japan': 'Japan', 'Jordan': 'Jordan',
                 'Kazakhstan': 'Kazakhstan', 'Kenya': 'Kenya',
                 'Kiribati': 'Kiribati', 'Kuwait': 'Kuwait',
                 'Kyrgyzstan': 'Kyrgyzstan', 'Laos': 'Laos', 'Latvia': 'Latvia',
                 'Lebanon': 'Lebanon', 'Lesotho': 'Lesotho',
                 'Liberia': 'Liberia', 'Libya': 'Libya',
                 'Liechtenstein': 'Liechtenstein', 'Lithuania': 'Lithuania',
                 'Luxembourg': 'Luxembourg', 'Macedonia': 'Republic_of_Macedonia',
                 'Madagascar': 'Madagascar', 'Malawi': 'Malawi',
                 'Malaysia': 'Malaysia', 'Maldives': 'Maldives', 'Mali': 'Mali',
                 'Malta': 'Malta', 'Marshall Islands': 'Marshall_Islands',
                 'Mauritania': 'Mauritania', 'Mauritus': 'Mauritus',
                 'Mexico': 'Mexico', 'Micronesia': 'Micronesia',
                 'Moldova': 'Moldova', 'Monaco': 'Monaco',
                 'Mongolia': 'Mongolia', 'Montenegro': 'Montenegro',
                 'Morocco': 'Morocco', 'Mozambique': 'Mozambique',
                 'Myanmar': 'Myanmar', 'Namibia': 'Namibia', 'Nauru': 'Nauru',
                 'Nepal': 'Nepal', 'Kingdom of the Netherlands': 'Kingdom_of_the_Netherlands',
                 'New Zealand': 'New_Zealand', 'Nicaragua': 'Nicaragua',
                 'Niger': 'Niger', 'Nigeria': 'Nigeria', 'North Korea': 'North_Korea',
                 'Norway': 'Norway', 'Oman': 'Oman', 'Pakistan': 'Pakistan',
                 'Palau': 'Palau', 'Palestine': 'State_of_Palestine',
                 'Panama': 'Panama', 'Papua New Guinea': 'Papua_New_Guinea',
                 'Paraguay': 'Paraguay', 'Peru': 'Peru',
                 'Philippines': 'Philippines', 'Poland': 'Poland',
                 'Portugal': 'Portugal', 'Qatar': 'Qatar', 'South Korea': 'South_Korea',
                 'Republic of the Congo': 'Republic_of_the_Congo',
                 'Romania': 'Romania', 'Russia': 'Russia', 'Rwanda': 'Rwanda',
                 'Saint Kitts and Nevis': 'Saint_Kitts_and_Nevis',
                 'Saint Lucia': 'Saint_Lucia',
                 'Saint Vincent and the Grenadines': 'Saint_Vincent_and_the_Grenadines',
                 'Samoa': 'Samoa', 'San Marino': 'San_Marino',
                 'Sao Tome and Principe': 'Sao_Tome_and_Principe',
                 'Saudi Arabia': 'Saudi_Arabia', 'Senegal': 'Senegal',
                 'Serbia': 'Serbia', 'Seychelles': 'Seychelles',
                 'Sierra Leone': 'Sierra_Leone', 'Singapore': 'Singapore',
                 'Slovakia': 'Slovakia', 'Slovenia': 'Slovenia',
                 'Solomon Islands': 'Solomon_Islands', 'Somalia': 'Somalia',
                 'South Africa': 'South_Africa', 'South Korea': 'South_Korea',
                 'South Sudan': 'South_Sudan', 'Spain': 'Spain', 'Sri Lanka': 'Sri_Lanka',
                 'Sudan': 'Sudan', 'Suriname': 'Suriname', 'Swaziland': 'Swaziland',
                 'Sweden': 'Sweden', 'Switzerland': 'Switzerland', 'Syria': 'Syria',
                 'Taiwan': 'Taiwan', 'Tajikistan': 'Tajikistan', 'Tanzania': 'Tanzania',
                 'Thailand': 'Thailand', 'East Timor': 'East_Timor', 'Togo': 'Togo',
                 'Tonga': 'Tonga', 'Transnistria': 'Transnistria',
                 'Trinidad and Tobago': 'Trinidad_and_Tobago',
                 'Tunisia': 'Tunisia', 'Turkey': 'Turkey', 'Turkmenistan': 'Turkmenistan',
                 'Tuvalu': 'Tuvalu', 'Uganda': 'Uganda', 'Ukraine': 'Ukraine',
                 'United Arab Emirates': 'United_Arab_Emirates',
                 'United Kingdom': 'United_Kingdom', 'United States': 'United_States',
                 'Uruguay': 'Uruguay', 'Uzbekistan': 'Uzbekistan',
                 'Vanuatu': 'Vanuatu', 'Vatican City': 'Vatican_City',
                 'Venezuela': 'Venezuela', 'Vietnam': 'Vietnam',
                 'Yemen': 'Yemen', 'Zambia': 'Zambia', 'Zimbabwe': 'Zimbabwe'}


country = random.choice(list(dictCountries.keys()))


def get_dictionary(country):
    webpage = urllib.request.urlopen('https://en.wikipedia.org/wiki/%s' % dictCountries.get(country))
    soup = BeautifulSoup(webpage, 'lxml')
    pageinfobox = soup.find('table', {'class': 'infobox'})
    entries = pageinfobox.findAll('tr')
    dictOfEntries = {}
    for entry in entries:
        if entry.find('th', {'scope': 'row'}):
            question_key = entry.find('th', {'scope': 'row'}).getText().replace('\n', ' ')
            answer_value = entry.find('td').getText()
            dictOfEntries[question_key] = answer_value
            return dictOfEntries


def get_capital(country):
    dictOfEntries = get_dictionary(country)
    if 'Capital' in dictOfEntries:
        return(dictOfEntries['Capital'])
    if 'Capital and largest city' in dictOfEntries:
        return(dictOfEntries['Capital and largest city'])
    else:
        return(dictOfEntries)


window = Tk()
window.title("Do you know your capitals?")
window.geometry("500x500")


question = tkinter.Label(window, text = "What is the capital of %s?" % country)
question.place(x = 5, y = 5)


def result(txt):
    if txt == get_capital(country):
        msg = messagebox.showinfo('Wow', "You're right!")
    else:
        msg = messagebox.showinfo('NO', "WRONG!")


Atxt = 0
Btxt = 0
Ctxt = 0
Dtxt = 0
buttons = [Atxt, Btxt, Ctxt, Dtxt]


def choose_correct():
    val = [0, 1, 2, 3]
    correct = random.choice(val)
    return correct


correct = choose_correct()
buttons[correct] = get_capital(country)


if buttons[0] != buttons[correct]:
    buttons[0]= get_capital(random.choice(list(dictCountries.keys())))
if buttons[1] != buttons[correct]:
    buttons[1]= get_capital(random.choice(list(dictCountries.keys())))
if buttons[2] != buttons[correct]:
    buttons[2]= get_capital(random.choice(list(dictCountries.keys())))
if buttons[3] != buttons[correct]:
    buttons[3]= get_capital(random.choice(list(dictCountries.keys())))


Atxt = buttons[0]
Btxt = buttons[1]
Ctxt = buttons[2]
Dtxt = buttons[3]


A = Button(window, text=Atxt, command=lambda: result(Atxt))
A.place(x=50, y=50)
# A.pack()


B = Button(window, text=Btxt, command=lambda: result(Btxt))
B.place(x=50, y=100)
# B.pack()

C = Button(window, text=Ctxt, command=lambda: result(Ctxt))
C.place(x=50, y=150)
# C.pack()

D = Button(window, text=Dtxt, command=lambda: result(Dtxt))
D.place(x=50, y=200)
# D.pack()

window.mainloop()
