#kendi oluşturduğum modül
#python da hazır olarak bulunan modül
#pip'de => geliştiriciler tarafından oluşturulan daha sonra da projeye dahil edilerek kullanılan modül 

from classes import Human
import random #pythondaki hazır modüller
#import openpyxl #hazır paket modüller

human1 = Human("irem",25)
human1.talk("selam")

print(random.random())