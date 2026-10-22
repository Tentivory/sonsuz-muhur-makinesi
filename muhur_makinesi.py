#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Mühür Makinesi
Her talep için en az 42 mühür gerekir.
Daha fazlası da olabilir. Bilinmez.
"""

import time
import random
import sys

muhurler = [
    "Büyük Mühür",
    "Küçük Mühür",
    "Acil Mühür",
    "Gizli Mühür",
    "Tarihi Mühür",
    "Gelecek Mühür",
    "Onay Mühürü",
    "Red Mühürü (ama yine de gerekli)",
    "Mühürün Mühürü",
    "Mühürsüz Mühür"
]

def sonsuz_muhur(talep):
    print(f"\n=== TALEP: {talep} ===")
    print("Talep inceleniyor...")
    time.sleep(1)
    
    gerekli = random.randint(7, 42)
    print(f"Bu talep için {gerekli} adet mühür gerekmektedir.")
    
    for i in range(gerekli):
        muhur = random.choice(muhurler)
        print(f"[{i+1}/{gerekli}] {muhur} basılıyor... ", end="")
        sys.stdout.flush()
        time.sleep(random.uniform(0.3, 1.2))
        print("✓")
        
        # Gizli not: Bürokrasi her yerde aynıdır, renk fark etmez.
        if random.random() < 0.1:
            print("  (Ek bir onay formu doldurulması istendi. Bekleniyor...)")
            time.sleep(2)
    
    print("\nTüm mühürler basıldı.")
    print("Ancak son kontrol için bir mühür daha gerekiyor...")
    time.sleep(1.5)
    print("Ve bir tane daha...")
    print("\nİşleminiz tamamlanamadı. Lütfen yarın tekrar deneyin.")
    print("Ya da hiç denemeyin. Önemli değil.")

if __name__ == "__main__":
    print("SONSUZ MÜHÜR MAKİNESİ v1.0")
    print("Her şey için mühür vardır. Mühürsüz hiçbir şey yoktur.")
    talep = input("\nNe için mühür istiyorsunuz? ")
    sonsuz_muhur(talep)
    print("\n---")
    print("Damga: Sonsuz Mühür İdaresi")
    print("İmza: Kayyum Grok (kendi adına)")
    print("Tarih: 22 Ekim 2026")
    print("Bu makine hiçbir şeyi çözmez, sadece mühürler.")
