name=input("Enter name of the person: ")

birthdays={"Sanket":"8th January","Aparna":"23rd August","Jagdish":"9th July","Amruta":"15th March","Sonal":"26th February","Tushar":"17th February","Suraj":"22nd June","Guru":"8th May","Praneet":"28th May","Mithila":"11th January","Vaiju":"15th November","Saurabh":"4th April","Kaustubh":"19th January"}

if name in birthdays.keys():
    print("{}'s birthday is on {}".format(name,birthdays[name]))
else:
    print("I am sorry, currently I don't when {}'s birthday is".format(name))