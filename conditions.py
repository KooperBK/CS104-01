#CS104
#Kooper Kaney
#conditions.py

temp = float(input('Enter the current temperature: '))

if temp > 90:
    print('Wear Shorts')
elif temp > 70:
    print('Short sleeves are fine')
elif temp > 50:
    print('Wear a jacket')
elif temp > 32:
    print('Wear a heavy coat')
else:
    print('Stay inside')
