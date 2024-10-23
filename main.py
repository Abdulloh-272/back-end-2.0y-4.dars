


talabalar = []

while True:
 create = input('Talaba qoshish: ')
 if create == 'stop':
  break
 talabalar.append(create)


for i in talabalar:
  print(i)

name =  input('Ism kiriting: ')
if name in talabalar:
  talabalar.remove(name)

talabalar.sort()
for i in talabalar:
  print(i)
print()
for x in range(len(talabalar)-1,-1,-1):
  print(talabalar[x])



