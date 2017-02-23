print "Come ti chiami?"
name = raw_input() 

print "Ciao", name
print "Ciao %s. Quanti anni hai?" % name
age = int(raw_input())
print "Ti odio %s di %s anni" % (name, age)

print """
Ecco cosa mi hai detto:
nome: %s (tipo %s)
eta': %s (tipo %s)
""" % (name, type (name), age, type (age))

bdate = 2017 - age

print "Quindi sei stato abortito nel " , bdate

place = raw_input("Dove sei nato?")

print "Fa un po' schifo %s meglio Tenerife" % (place)
