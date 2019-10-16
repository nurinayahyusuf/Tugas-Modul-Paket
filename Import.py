import Anaya

def main () :
    jarijari = 4
    
    volume = Anaya.volumeBola (jarijari)
    luas = Anaya.luasBola (jarijari)
    
    print ("BOLA")
    print ("Jari-Jari\t : ", jarijari)
    print ("Volume\t : ", volume)
    print ("Luas\t : ", luas)
    
    R = 10
    
    volume = Anaya.volumeKubus (R)
    luas = Anaya.luasKubus (R)
    
    print ("KUBUS")
    print ("Rusuk\t : ", R)
    print ("Volume\t : ", volume)
    print ("Luas\t : ", luas)
    
    r = 4
    t = 6
    
    volume = Anaya.volumeTabung (r, t)
    luas = Anaya.luasSelimutTabung (r, t)
    
    print ("TABUNG")
    print ("Jari-Jari\t : ", r)
    print ("Tinggi\t : ", t)
    print ("Volume\t : ", volume)
    print ("Luas Selimut\t : ", luas)
    
if __name__ == "__main__" :
    main ()
