# 🚨 SERPER API KEY SORUNU

## ❌ İki API Key de Çalışmıyor!

```
Key 1: e5d96221af2e878405bca03a92a5305279303bf60b34896b8744104b1f417767 ❌
Key 2: 565ba773bb1936acdc2ef328ea8df5a8a952178ad7cd0b3bbeaa287fb69d2fe6 ❌
```

Her ikisi de **403 Unauthorized** hatası veriyor!

## 🔍 Neden?

### Olasılık 1: Key'ler Eski/Süresi Dolmuş
- Key'ler daha önce alınmış ama süresi dolmuş
- Hesap silinmiş veya devre dışı bırakılmış

### Olasılık 2: Key'ler Yanlış
- Copy-paste hatası
- Eksik veya fazla karakter
- Bozuk format

### Olasılık 3: Serper Hesabı Yok
- Hiç hesap oluşturulmamış
- Sadece key alınmış ama hesap aktif değil

## ✅ KESİN ÇÖZÜM: Sıfırdan Başla

### ADIM 1: Tarayıcıyı Aç
Chrome, Firefox veya Edge'i açın

### ADIM 2: Serper.dev'e Git
```
https://serper.dev
```

### ADIM 3: Kayıt Ol (Sign Up)
1. Sağ üstte **"Sign Up"** butonuna tıkla
2. Email adresini gir
3. Şifre oluştur
4. Veya **"Sign up with Google"** butonuna tıkla (daha kolay)

### ADIM 4: Email Doğrulama
- Email kutunu kontrol et
- Serper'dan gelen doğrulama linkine tıkla
- Email'i onayla

### ADIM 5: Giriş Yap (Login)
- https://serper.dev/dashboard adresine git
- Email ve şifre ile giriş yap

### ADIM 6: API Key Al
1. Dashboard'da sol menüden **"API Keys"** tıkla
2. **"Create API Key"** butonuna bas
3. Key otomatik oluşturulur
4. **"Copy"** butonuna bas veya key'i seçip kopyala

### ADIM 7: Key'i Test Et
```bash
# Yeni key'i buraya yapıştır
python test-real-sites.py
```

## 📸 Görsel Rehber

```
1. serper.dev → Sign Up
2. Email/Google ile kayıt
3. Email doğrula
4. Dashboard → API Keys
5. Create API Key
6. Copy Key
7. Bot'a yapıştır
```

## 💡 Önemli Notlar

✅ **Ücretsiz Plan**: 2,500 arama/ay
✅ **Kredi Kartı Gerekmez**: Ücretsiz kayıt
✅ **Anında Aktif**: Kayıt olunca hemen kullanabilirsin
✅ **Dashboard'dan Takip**: Kaç arama kaldığını görebilirsin

## ⚠️ Yaygın Hatalar

### ❌ Yanlış:
- Başka birinin API Key'ini kullanmak
- Eski/bilinmeyen bir key kullanmak
- Key'i yanlış kopyalamak (eksik karakter)

### ✅ Doğru:
- Kendi hesabından yeni key oluşturmak
- Tüm karakterleri kopyalamak
- Dashboard'dan direkt "Copy" butonu kullanmak

## 🎯 Hızlı Test

Yeni key alınca test için:

```python
# test-serper-quick.py oluştur
import requests

API_KEY = "BURAYA_YENI_KEY_YAPISTIR"

response = requests.post(
    "https://google.serper.dev/search",
    headers={"X-API-KEY": API_KEY},
    json={"q": "test"}
)

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")

# 200 = ✅ Başarılı
# 403 = ❌ Hala yanlış key
```

## 📞 Yardım

Hala sorun varsa:
1. Serper hesabınızın aktif olduğunu kontrol edin
2. Dashboard'da kredi bakiyeniz var mı bakın
3. Email'inizin doğrulandığından emin olun
4. Yeni bir API Key oluşturup deneyin

---

**SONUÇ**: Kendi Serper hesabınızdan YENİ bir API Key almanız gerekiyor!
Verdiğiniz key'ler çalışmıyor.

👉 **Hemen**: https://serper.dev → Sign Up → API Key Al
