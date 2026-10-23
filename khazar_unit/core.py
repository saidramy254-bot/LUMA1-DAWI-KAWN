UTL_KM = 66866100.0
UTL_M = UTL_KM * 1000
UTL_INFO = {
    "symbol": "Øₜₗ",
    "origin": "33.0011N 7.614W - Wb80116",
    "doi": "10.5281/zenodo.23544275",
    "beacon": "1420MHz 1007 PULSARS"
}
def to_utl_km(km): return km / UTL_KM
def from_utl_km(utl): return utl * UTL_KM
