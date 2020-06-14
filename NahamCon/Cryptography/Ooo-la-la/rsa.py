from Crypto.Util.number import inverse
from factordb.factordb import FactorDB


n=3349683240683303752040100187123245076775802838668125325785318315004398778586538866210198083573169673444543518654385038484177110828274648967185831623610409867689938609495858551308025785883804091
e=65537
c=87760575554266991015431110922576261532159376718765701749513766666239189012106797683148334771446801021047078003121816710825033894805743112580942399985961509685534309879621205633997976721084983

f = FactorDB(n)
f.connect()

phi = 1
for x in f.get_factor_list():
	phi *= x-1


d=inverse(e,phi)
m=pow(c,d,n)
#print(m)#rawhex
print(bytes.fromhex(hex(m)[2:]).decode())#decodedtoascii





