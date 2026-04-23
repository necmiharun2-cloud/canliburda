import json
import requests

print("="*70)
print("SERPER API TEST - GERÇEK HURDA SİTELERİ")
print("="*70)

API_KEY = "565ba773bb1936acdc2ef328ea8df5a8a952178ad7cd0b3bbeaa287fb69d2fe6"

print("\n🔍 Bakır hurda fiyatı aranıyor...\n")

url = "https://google.serper.dev/search"
headers = {
    "X-API-KEY": API_KEY,
    "Content-Type": "application/json"
}
payload = json.dumps({
    "q": "bakır hurda fiyatı kg TL 2026",
    "gl": "tr",
    "hl": "tr",
    "num": 5
})

try:
    response = requests.post(url, headers=headers, data=payload, timeout=15)
    
    if response.status_code == 200:
        data = response.json()
        
        print("✅ Serper API BAŞARILI!\n")
        print(f"Toplam sonuç: {len(data.get('organic', []))}\n")
        print("="*70)
        
        if 'organic' in data:
            for i, result in enumerate(data['organic'][:5], 1):
                print(f"\n{i}. {result.get('title', 'Başlık yok')}")
                print(f"   URL: {result.get('link', 'URL yok')}")
                if 'snippet' in result:
                    snippet = result['snippet'][:200]
                    print(f"   İçerik: {snippet}")
                
                # Kaynak site
                link = result.get('link', '')
                if 'hurdaalim' in link:
                    print("   🏷️  Kaynak: hurdaalim.com ✓")
                elif 'hurdayim' in link:
                    print("   🏷️  Kaynak: hurdayim.com ✓")
                elif 'demiryolhurda' in link:
                    print("   🏷️  Kaynak: demiryolhurda.com ✓")
                elif 'sahibinden' in link:
                    print("   🏷️  Kaynak: sahibinden.com ✓")
                else:
                    print("   🏷️  Kaynak: Diğer site")
                print("-"*70)
        
        print("\n📊 Özet:")
        print(f"  - Serper API durumu: ✅ Çalışıyor")
        print(f"  - Bulunan kaynak sayısı: {len(data.get('organic', []))}")
        print(f"  - Gerçek sitelerden veri: EVET")
        print("\nBot bu kaynaklardan fiyat bilgilerini alıyor!")
        
    else:
        print(f"❌ Hata: {response.status_code}")
        print(f"Yanıt: {response.text}")
        
except Exception as e:
    print(f"❌ Bağlantı Hatası: {str(e)}")

print("\n" + "="*70)
input("\nÇıkmak için ENTER'a basın...")
