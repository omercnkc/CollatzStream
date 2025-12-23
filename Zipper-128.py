import os

class CollatzCipher:
    def __init__(self, n1, n2, burn_in=50):
        self.n1_init = n1
        self.n2_init = n2
        self.burn_in = burn_in

    def next_collatz(self, n):
        """Collatz adımını hesaplar: Çiftse n/2, Tekse 3n+1."""
        return n // 2 if n % 2 == 0 else 3 * n + 1

    def generate_block_key(self, s1, s2, s1_peak, s2_peak, size_bits=128):
        """Kayan (rolling) mantıkla 128 bitlik anahtar üretir."""
        bits_s1 = []
        bits_s2 = []
        target = size_bits // 2 # 64 bit birinden, 64 bit diğerinden

        # S1 yolu için 64 bit üret
        while len(bits_s1) < target:
            bit = '1' if s1 % 2 != 0 else '0'
            bits_s1.append(bit)
            s1 = self.next_collatz(s1)
            if s1 > s1_peak: s1_peak = s1
            
            if s1 == 1: # Onarma: S1 biterse güncel S2 ve kendi zirvesiyle çarp
                s1 = s1_peak * s2

        # S2 yolu için 64 bit üret
        while len(bits_s2) < target:
            bit = '1' if s2 % 2 != 0 else '0'
            bits_s2.append(bit)
            s2 = self.next_collatz(s2)
            if s2 > s2_peak: s2_peak = s2
            
            if s2 == 1: # Onarma: S2 biterse güncel S1 ve kendi zirvesiyle çarp
                s2 = s2_peak * s1

        # Fermuarlama (Interleaving): s1_0, s2_0, s1_1, s2_1...
        zippered_bits = "".join(b1 + b2 for b1, b2 in zip(bits_s1, bits_s2))
        key_int = int(zippered_bits, 2)
        
        return key_int, s1, s2, s1_peak, s2_peak

    def process_data(self, data, k1):
        """Şifreleme ve çözme işlemini senkronize şekilde yapar."""
        # Başlangıç durumu
        s1 = self.n1_init * k1
        s2 = self.n2_init * k1
        s1_peak, s2_peak = s1, s2
        
        # 1. Isınma (Burn-in): İlk 50 adımı atla
        for _ in range(self.burn_in):
            s1 = self.next_collatz(s1)
            s2 = self.next_collatz(s2)
            if s1 > s1_peak: s1_peak = s1
            if s2 > s2_peak: s2_peak = s2

        data_bytes = bytearray(data)
        output = bytearray()

        # 128 bitlik (16 byte) bloklar halinde ilerle
        for i in range(0, len(data_bytes), 16):
            block = data_bytes[i:i+16]
            
            # Güncel S1 ve S2'den 128 bitlik "kayan" anahtar üret
            key_int, s1, s2, s1_peak, s2_peak = self.generate_block_key(s1, s2, s1_peak, s2_peak)
            
            # Anahtarı byte dizisine çevir
            key_bytes = key_int.to_bytes(16, byteorder='big')
            
            # XOR işlemi (Kayan maske uygulaması)
            for j in range(len(block)):
                output.append(block[j] ^ key_bytes[j])
                
        return output

# --- KULLANIM ---

# 1. Gizli Anahtarlar (n1, n2)
secret_n1 = 31415926535897932384626433832795028841
secret_n2 = 27182818284590452353602874713526624977

cipher = CollatzCipher(secret_n1, secret_n2)

# 2. Şifreleme (Encryption)
original_text = "Bu mesaj Collatz kayan algoritması ile şifrelenmiştir."
random_k1 = int.from_bytes(os.urandom(4), byteorder='big') # 32-bit IV

encrypted_data = cipher.process_data(original_text.encode(), random_k1)

print("Orijinal Mesaj:", original_text)
print(f"K1 (IV): {random_k1}")
print(f"Şifreli (Hex): {encrypted_data.hex()[:60]}...")

# 3. Çözme (Decryption)
# Çözen kişi aynı n1, n2 ve mesajın başındaki k1'i kullanır
decrypted_data = cipher.process_data(encrypted_data, random_k1)

print(f"Çözülen Mesaj: {decrypted_data.decode()}")
