
s = input().strip()
vowels = 'AEIOU'
kevin = stuart = 0
L = len(s)
for i,ch in enumerate(s):
    if ch in vowels:
        kevin += L - i
    else:
        stuart += L - i
if kevin > stuart:
    print(f"Кевин {kevin}")
else:
    print(f"Стюарт {stuart}")
