# 🎯 YENİ SİSTEM - API'siz Google Scraping + Fiyat Değişimleri

## ✅ Tamamlanan Özellikler

### 1. **Google Scraping (Serper API YOK!)**
- ✅ Google'dan direkt hurda siteleri aranıyor
- ✅ İlk 10 sonuç otomatik scrape ediliyor
- ✅ hurdaalim.com, demiryolhurda.com gibi sitelerden fiyat çekiliyor
- ✅ BeautifulSoup ile HTML parse ediliyor
- ✅ **TAMAMEN ÜCRETSİZ** - API key gerekmez!

### 2. **Fiyat Değişim Takibi**
- ✅ Her fiyat karşılaştırması yapılıyor
- ✅ Önceki fiyatlar `fiyat-gecmis.json`'da saklanıyor
- ✅ Yeni fiyat ile eski fiyat karşılaştırılıyor

### 3. **Görsel Göstergeler**

#### Fiyat Yükseldiğinde (↑):
- **Yeşil ok** ▲ işareti
- **Yanıp sönen yeşil-beyaz** animasyon
- Yüzde gösterimi: `+5.2%`

#### Fiyat Düştüğünde (↓):
- **Kırmızı ok** ▼ işareti
- **Yanıp sönen kırmızı-beyaz** animasyon
- Yüzde gösterimi: `-3.1%`

## 🚀 Nasıl Çalışır?

### Bot Tarafı (bot.py):

```python
1. Bot başlatılır
   ↓
2. Google'dan hurda siteleri scrape edilir
   - hurdaalim.com
   - demiryolhurda.com
   - sahibinden.com
   - Google搜索结果 (ilk 10 site)
   ↓
3. Fiyatlar çıkarılır
   ↓
4. Önceki fiyatlarla karşılaştırılır
   - fiyat-gecmis.json'dan okunur
   ↓
5. Değişim yönü belirlenir
   - ↑ up (yeşil)
   - ↓ down (kırmızı)
   - → same (değişim yok)
   ↓
6. JSON'a eklenir
   {
     "n": "Soyulmuş Bakır",
     "p": 552.15,
     "change": "up",
     "percent": 5.2
   }
   ↓
7. Sunucuya gönderilir
   ↓
8. Yeni fiyatlar kaydedilir (gelecek karşılaştırma için)
```

### Frontend Tarafı (index.html):

```javascript
1. fiyatlar.json yüklenir
   ↓
2. Her item için change kontrolü:
   - item.change === 'up' → Yeşil animasyon ▲
   - item.change === 'down' → Kırmızı animasyon ▼
   ↓
3. CSS animasyonları:
   - blink-green-white (yeşil-beyaz yanıp söner)
   - blink-red-white (kırmızı-beyaz yanıp söner)
   ↓
4. Kullanıcı görür:
   ↑ +5.2%  (yeşil yanıp sönüyor)
   ↓ -3.1%  (kırmızı yanıp sönüyor)
```

## 📊 Örnek Çıktı

### Bot Log:
```
==================================================
FİYAT DEĞİŞİMLERİ
==================================================
↑ BAKIR HURDASI__Soyulmuş Bakır: 520.00 → 552.15 (+6.2%)
↓ DEMIR__DKP: 13.50 → 12.20 (-9.6%)
↑ ALÜMINYUM__Profil: 95.00 → 99.10 (+4.3%)

Özet: 8 yükseldi, 3 düştü
```

### Frontend Görünüm:
```
Soyulmuş Bakır         552.15 TL ▲ +6.2% (yeşil yanıp sönüyor)
DKP                    12.20 TL  ▼ -9.6% (kırmızı yanıp sönüyor)
Profil                 99.10 TL  ▲ +4.3% (yeşil yanıp sönüyor)
```

## 🎨 CSS Animasyonları

### Yükselen Fiyat (Yeşil):
```css
@keyframes blink-green-white {
    0%, 100% { background: transparent; }
    50% { background: #10b981; }  /* Yeşil */
}
```

### Düşen Fiyat (Kırmızı):
```css
@keyframes blink-red-white {
    0%, 100% { background: transparent; }
    50% { background: #ef4444; }  /* Kırmızı */
}
```

## 📁 Dosyalar

- `bot.py` - Ana bot (Google scraping + fiyat karşılaştırma)
- `index.html` - Frontend (animasyonlu göstergeler)
- `fiyatlar.json` - Güncel fiyatlar
- `fiyat-gecmis.json` - Fiyat geçmişi (otomatik oluşturulur)
- `fiyat-alici.php` - Backend API

## 💡 Avantajlar

✅ **Ücretsiz** - Serper API yok, ücret yok
✅ **Otomatik** - Her saat güncelleme
✅ **Görsel** - Yanıp sönen oklar
✅ **Takip** - Fiyat değişimi yüzdesi
✅ **Basit** - API key gerekmez
✅ **Gerçek** - Gerçek sitelerden veri

## 🔍 Scrap Edilen Siteler

1. **hurdaalim.com** - Hurda alım-satım
2. **demiryolhurda.com** - Hurda ticaret
3. **sahibinden.com** - İlan sitesi
4. **Google İlk 10 Sonuç** - Organik arama sonuçları

## 🎯 Kullanım

```bash
# Bot'u başlat
python bot.py

# BAŞLAT butonuna bas
# Bot otomatik:
# 1. Google'dan fiyatları çeker
# 2. Önceki fiyatlarla karşılaştırır
# 3. Değişim yönünü belirler
# 4. Sunucuya gönderir
# 5. Frontend'de yanıp sönen oklar görünür!
```

## 📈 Gelecek İyileştirmeler

- [ ] Daha fazla site scrape
- [ ] Regex ile daha iyi fiyat çıkarma
- [ ] JavaScript rendering (Selenium)
- [ ] Cron job ile otomatik güncelleme
- [ ] Email bildirimleri (büyük değişimlerde)

---

**SONUÇ**: Artık **API olmadan** gerçek sitelerden fiyat çekiyorsunuz
ve **yanıp sönen oklarla** fiyat değişimlerini görüyorsunuz! 🎉
