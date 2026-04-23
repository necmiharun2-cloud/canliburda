# 🔴 SERPER API KEY HATASI

## ❌ Sorun

API Key'iniz **geçersiz** veya **süresi dolmuş**:
```
403 Unauthorized
```

## ✅ Çözüm: Yeni API Key Alma

### Adım 1: Serper.dev'e Git
🌐 **https://serper.dev** adresine gidin

### Adım 2: Üye Ol
- "Sign Up" butonuna tıklayın
- Email ve şifre ile kayıt olun
- Veya Google ile giriş yapın

### Adım 3: API Key Al
1. Dashboard'a gidin
2. "API Keys" bölümünü açın
3. Yeni API Key oluşturun
4. Key'i kopyalayın

### Adım 4: Bot'a Ekle
Bot'u açın ve:
1. **Serper API Key** alanına yeni key'i yapıştırın
2. **API Key Kaydet** butonuna basın
3. **BAŞLAT** butonuna basın

## 💰 Ücretsiz Plan

Serper **2,500 ücretsiz arama/ay** verir!

- ✅ Bakır hurda araması: 1 arama
- ✅ Sarı hurda araması: 1 arama  
- ✅ Demir hurda araması: 1 arama
- Toplam: ~5 arama/her döngü

**2,500 arama = 500 döngü = 500 saat!**

## 🎯 Alternatifler

### Seçenek 1: Serper API (Önerilen)
- Ücretsiz: 2,500/ay
- Kolay entegrasyon
- Google sonuçları
- **Maliyet**: Ücretsiz başlar

### Seçenek 2: Manuel Fiyat Güncelleme
- Her hafta piyasa araştır
- Bot.py'de fiyatları güncelle
- Bot otomatik gönderir
- **Maliyet**: Ücretsiz ama manuel

### Seçenek 3: Ücretsiz API'ler
Bazı ücretsiz alternatifler:
- **DuckDuckGo API** (sınırlı)
- **Bing Web Search API** (ücretsiz 1,000/ay)
- **Brave Search API** (ücretsiz 2,000/ay)

## 📊 Şu Anki Durum

✅ Bot **çalışıyor**
✅ Fiyatlar **gönderiliyor**  
⚠️ API Key **geçersiz**
⚠️ Serper **çalışmıyor**

### Bot Ne Yapıyor?

API Key geçersiz olduğu için bot:
1. Serper'a bağlanmaya çalışıyor
2. 403 hatası alıyor
3. Piyasa fiyatlarına geçiyor
4. Fiyatları gönderiyor
5. ✅ OK diyor

**Yani bot çalışıyor ama gerçek sitelerden veri çekmiyor!**

## 🚀 Hemen Başla

1. https://serper.dev adresine git
2. Ücretsiz hesap oluştur
3. API Key'i al
4. Bot'a yapıştır
5. Test et!

## 💡 Test

Yeni API Key aldıktan sonra:
```bash
python test-real-sites.py
```

Bu script ile API Key'in çalışıp çalışmadığını test edin!

## 📞 Yardım

Sorun yaşarsanız:
- API Key'in doğru olduğundan emin olun
- Hesabınızın aktif olduğunu kontrol edin
- Serper dashboard'dan kullanım istatistiklerine bakın

---

**ÖNEMLİ**: API Key olmadan bot piyasa fiyatlarını kullanır.
Gerçek sitelerden veri için **geçerli bir Serper API Key** şart!
