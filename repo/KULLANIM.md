# Hurda Bot - Serper API Entegrasyonu

## ✅ Yapılan Değişiklikler

Bot artık **Serper API** ile gerçek piyasa verisi çekecek şekilde güncellendi!

### Yeni Özellikler:

1. **Serper API Entegrasyonu**: Google'dan gerçek hurda fiyatları arama
2. **API Key Yönetimi**: GUI'den API key girme ve kaydetme
3. **Akıllı Fiyat Çıkarma**: Arama sonuçlarından fiyat bilgisi ayıklama
4. **Hata Yönetimi**: API çalışmazsa varsayılan fiyatlar kullanılır

## 🚀 Kullanım

### 1. Serper API Key Alma

1. https://serper.dev adresine gidin
2. Ücretsiz hesap oluşturun
3. Dashboard'dan API Key'inizi kopyalayın

### 2. Bot'u Çalıştırma

```bash
python bot.py
```

### 3. API Key Girme

Bot GUI açıldığında:
1. **Serper API Key** alanına key'inizi girin
2. **API Key Kaydet** butonuna basın
3. **Yüzde Ekle (%)** alanına kar marjınızı girin (opsiyonel)
4. **BAŞLAT** butonuna basın

### 4. Test Etme

Serper bağlantısını test etmek için:

```bash
python test-serper.py
```

## 📋 Nasıl Çalışır?

1. Bot çalıştığında Serper API'ye sorgu gönderir
2. Google'dan güncel hurda fiyatları aranır
3. Arama sonuçlarından fiyat bilgileri çıkarılır
4. Gerçek fiyatlar `fiyat-alici.php`'ye gönderilir
5. Frontend (`index.html`) bu verileri gösterir

## 🔧 API Kullanımı

### Serper API Çağrısı:
```python
url = "https://google.serper.dev/search"
headers = {
    "X-API-KEY": "YOUR_API_KEY",
    "Content-Type": "application/json"
}
payload = {"q": "bakır hurda fiyatı TL 2026", "gl": "tr", "hl": "tr"}
```

### Arama Sorguları:
- Bakır hurda fiyatı
- Sarı hurda fiyatı
- Demir hurda fiyatı
- Alüminyum hurda fiyatı
- Kablo hurda fiyatı

## ⚠️ Önemli Notlar

1. **Serper API Ücretsiz Plan**: 2,500 ücretsiz arama/ay
2. **API Key Güvenliği**: Key'inizi kimseyle paylaşmayın
3. **Yedek Sistem**: API çalışmazsa varsayılan fiyatlar kullanılır
4. **Güncelleme Sıklığı**: Bot saatlik güncelleme yapar

## 🧪 Test

Bot'u test etmek için:

1. Bot'u başlatın: `python bot.py`
2. API Key'inizi girin
3. BAŞLAT butonuna basın
4. Log penceresinde "Gerçek fiyatlar alınıyor..." mesajını görün
5. `fiyatlar.json` dosyasının güncellendiğini kontrol edin

## 📊 Fiyat Verisi Yapısı

```json
{
  "t": "BAKIR HURDASI",
  "i": [
    {"n": "Soyulmuş Bakır", "p": 552.15},
    {"n": "Lama Bakır", "p": 522.34}
  ]
}
```

- `t`: Kategori başlığı
- `i`: Ürün listesi
- `n`: Ürün adı
- `p`: Fiyat (TL)

## 🎯 Sonraki Adımlar

Daha gelişmiş kullanım için:
1. Serper'den gelen snippet'lerden fiyat parse etme geliştirilebilir
2. Özel web sitelerinden scraping eklenebilir
3. Fiyat değişikliklerinde bildirim sistemi eklenebilir

## 💡 Sorun Giderme

**Serper API Hatası:**
- API Key'inizi kontrol edin
- İnternet bağlantınızı kontrol edin
- Serper limitinizi kontrol edin

**Bot Çalışmıyor:**
- `pip install requests` komutunu çalıştırın
- Python sürümünüzü kontrol edin (3.7+)

**Fiyatlar Güncellenmiyor:**
- `fiyat-alici.php` dosyasının yazma izinlerini kontrol edin
- Server loglarını kontrol edin

## 📞 Destek

Sorun yaşarsanız:
- Log penceresindeki hataları kontrol edin
- `test-serper.py` ile API bağlantısını test edin
- Serper dashboard'dan kullanım istatistiklerini kontrol edin
