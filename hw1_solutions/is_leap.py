
year = int(input())
def is_leap(y):
    return (y%400==0) or (y%4==0 and y%100!=0)
print(is_leap(year))
