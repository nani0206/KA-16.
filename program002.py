def next_date(year, month, day):
 if not (1 <= year <= 9999):
  raise ValueError("Invalid year")
 if not (1 <= month <= 12):
  raise ValueError("Invalid month")
 if not (1 <= day <= 31):
  raise ValueError("Invalid day")
if month in [1, 3, 5, 7, 8, 10, 12]:
 if day < 31:
   return year, month, day + 1
 else:
   return year, month + 1, 1
 elif month == 2:
if year % 4 == 0 and (year % 100!= 0 or year % 400 == 0):
   if day < 29:
     return year, month, day + 1
  else:
     return year, month + 1, 1
  else:
     if day < 28:
     return year, month, day + 1
  else:
     return year, month + 1, 1
  else:
     if day < 30:
     return year, month, day + 1
  else:
     return year, month + 1, 1

 if month == 12:
  return year + 1, 1, 1
 else:
  return year, month + 1, 1
# Test cases
print("Valid dates:")
print(next_date(2022, 6, 15)) # (2022, 6, 16)
print(next_date(2022, 6, 30)) # (2022, 7, 1)
print(next_date(2022, 12, 31)) # (2023, 1, 1)
print(next_date(2020, 2, 28)) # (2020, 2, 29)
print(next_date(2019, 2, 28)) # (2019, 3, 1)
print("\nInvalid dates:")
try:
 print(next_date(0, 6, 15)) # Error
except ValueError as e:
 print(e)
try:
 print(next_date(2022, 13, 15)) # Error
except ValueError as e:
 print(e)
try:
 print(next_date(2022, 6, 32)) # Error
except ValueError as e:
 print(e)