
human_age= float(input("enter human age: "))
dog_life = human_age * 7 #14.7 14+0.7
#print(dog_life
dog_years= int(dog_life) #14

dog_months=int((dog_life-dog_years)*12)  #0.7*12=8.4 = 8

dog_days= ((dog_life-dog_years)*12)-(dog_months) 
dog_days=int(dog_days*30) #12

#print(f"Dog age is {dog_years:.2f} years {dog_months:.2f} months {dog_days:.2f} days")
'''
'''
human_age=("enter your age")  
#cat_life= (human_age/9)
#print(cat_life)
'''

human_years=float(input("enter_human_age"))
cat_years=float(human_years//9)
print(cat_years) 
'''  
'''
yearss=int(cat_years)
floatmonthss=(cat_years-yearss)
monthss=floatmonthss*12
month=int(monthss)
monthss=monthss-int(monthss)
dayss=monthss*30
day=(int(dayss))
#print(f' age is {int(yearss)} years {int(monthss)} months {int(day)} days')
'''

human_years=float(input("enter age in human years"))
horse_age=((((human_years)**2) -47/7 +12)*3)
years=int(horse_age)
floatmonth= (horse_age-years)
monthsintermofyears=floatmonth * 12
month= (int(monthsintermofyears))
monthsintermsofyears =monthsintermofyears -int(monthsintermofyears)
daysintermsofmonths=monthsintermofyears * 30
day = (int(daysintermsofmonths))
#print(monthsintermsofyears)
print(f'your age in horse yearsis {int(years)} years {int(month)} months {int(day)} days')

  
          
