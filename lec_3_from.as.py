from lec_3_my_module import earth_mass as em
from lec_3_my_module import sigma_steff_bolc as G
from lec_3_my_module import gravity_constant as sigma

g = em * G / 10*2
print(g)

x = em * G * sigma
print(x)