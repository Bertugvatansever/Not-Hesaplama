sınav1=int(input("1.sınav notunu giriniz.\n"))
sınav2=int(input("2.sınav notunu giriniz.\n"))
ortalama=(sınav1+sınav2)/2
if (ortalama>0 and ortalama<=24):
    print("5 lik sistemden '0' aldınız.")
elif(ortalama>24 and ortalama<=44):
    print("5 lik sistemden '1' aldınız.")
elif(ortalama>44 and ortalama<=54):
    print("5 lik sistemden '2' aldınız.")
elif(ortalama>54 and ortalama<=69):
    print("5 lik sistemden '3' aldınız.")
elif(ortalama>69 and ortalama<=84):
    print("5 lik sistemden '4' aldınız.")
elif(ortalama>84 and ortalama<=100):
    print("5 lik sistemden '4' aldınız.")
