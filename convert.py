f = open("mga.txt","r")
lines = f.readlines()
f.close()
f = open("mga-x.txt","w")
check=2
for line in lines:
  line = line.strip(' \t\r')
  if line=="Previous Chapter Next Chapter"+"\n":
    check+=1
  if check!=2:
    f.write(line)
  if line=="Email Address"+"\n":
   check=0
f.close()
