me="Sanket"
intro= "Let's Start with the class!!"

greetings="Welcome to Python Class Mr. %s, %s"%(me,intro)
print(greetings)

a= "Welcome to Python Class Mr. {}, {}"
greetings1= a.format(me, intro)
print(greetings1)

b= "Welcome to Python Class Mr. {1}, {0}"
greetings1= b.format(me, intro)
print(greetings1)

c= f"Welcome to Python Class Mr.{me}, {intro}"
print(c)

today="Monday"
date="2nd August"
welcome= f"Welcome Mr. Kulkarni, your meeting schedule for {today}, the {date} is empty. Have a good day!"
print(welcome)