num = 178615
dia = num // (24*60*60)
res = dia * 24
hs = num // (60*60) - res
res = (res + hs) * 60
min = num // 60 - res
res = (res + min) * 60
seg = num // 1 - res
print('No número {} cabe {} dias {} hora, {} minutos e {} segundos'.format(num, dia, hs, min, seg))

