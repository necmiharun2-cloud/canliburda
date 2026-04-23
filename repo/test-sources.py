import json
import requests

print("="*70)
print("HURDA BOT - KAYNAK SİTELER ve SERPER ENTEGRASYONU")
print("="*70)

print("\n📊 FİYAT KAYNAKLARI:")
print("-"*70)

websites = [
    ("Serper API (Google Arama)", "https://google.serper.dev", "Google'dan sonuçlar"),
    ("hurdayim.com", "https://www.hurdayim.com", "Hurda alım-satım sitesi"),
    ("hurdaalim.com", "https://www.hurdaalim.com", "Hurda alım firmaları"),
    ("sahibinden.com", "https://www.sahibinden.com", "İlan sitesi"),
    ("demiryolhurda.com", "https://www.demiryolhurda.com", "Hurda ticaret"),
    ("milliyet.com.tr", "https://www.milliyet.com.tr/ekonomi", "Ekonomi haberleri"),
]

for i, (name, url, desc) in enumerate(websites, 1):
    print(f"\n{i}. {name}")
    print(f"   URL: {url}")
    print(f"   Açıklama: {desc}")

print("\n\n🔍 SERPER ARAMA SORGULARI:")
print("-"*70)

queries = [
    "bakır hurda fiyatı bugün TL site:hurdayim.com OR site:hurdaalim.com",
    "sarı hurda pirinç fiyatı TL 2026",
    "demir hurda fiyatı kg TL",
    "alüminyum hurda fiyatı TL",
    "kablo hurda fiyatı TL",
]

for i, query in enumerate(queries, 1):
    print(f"\n{i}. {query}")

print("\n\n" + "="*70)
print("NOT: Bot şu anda Serper API kullanıyor.")
print("Serper, Google'dan sonuçları çekip size gösteriyor.")
print("Fiyatlar bu sitelerden aranarak bulunuyor.")
print("="*70)

# Test Serper
api_key = input("\nSerper API Key'iniz varsa girin (test için, boş geçilebilir): ").strip()

if api_key:
    print("\n🧪 Serper API Test Ediliyor...\n")
    
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "q": "bakır hurda fiyatı TL",
        "gl": "tr",
        "hl": "tr",
        "num": 5
    })
    
    try:
        response = requests.post(url, headers=headers, data=payload, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Serper API Bağlantısı BAŞARILI!\n")
            
            if 'organic' in data:
                print(f"Bulunan sonuçlar: {len(data['organic'])}\n")
                
                for i, result in enumerate(data['organic'][:5], 1):
                    print(f"{i}. {result.get('title', 'Başlık yok')}")
                    print(f"   Site: {result.get('link', 'URL yok')}")
                    if 'snippet' in result:
                        snippet = result['snippet'][:200]
                        print(f"   İçerik: {snippet}...")
                    print()
        else:
            print(f"❌ Hata: {response.status_code}")
            print(f"Yanıt: {response.text}")
            
    except Exception as e:
        print(f"❌ Bağlantı Hatası: {str(e)}")
else:
    print("\n⚠️  API Key girilmedi. Test yapılmadı.")
    print("Bot'u çalıştırıp GUI'den API Key girebilirsiniz.")

print("\n" + "="*70)
